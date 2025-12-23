/**
 * Express server for TikTok landing page
 * Handles email subscriptions and TikTok Events API
 */

const express = require('express');
const cors = require('cors');
const fs = require('fs').promises;
const path = require('path');
const crypto = require('crypto');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname))); // Serve from root directory

// Serve landing page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Configuration (set these in .env)
const TIKTOK_PIXEL_ID = process.env.TIKTOK_PIXEL_ID || 'YOUR_PIXEL_ID';
const TIKTOK_ACCESS_TOKEN = process.env.TIKTOK_ACCESS_TOKEN || '';
const TIKTOK_API_VERSION = 'v1.3';
const TIKTOK_EVENTS_API_URL = `https://business-api.tiktok.com/open_api/${TIKTOK_API_VERSION}/event/track/`;

// Data storage (in production, use a database)
const DATA_DIR = path.join(__dirname, 'data');
const EMAILS_FILE = path.join(DATA_DIR, 'emails.json');
const EVENTS_FILE = path.join(DATA_DIR, 'events.json');

// Ensure data directory exists
async function ensureDataDir() {
    try {
        await fs.mkdir(DATA_DIR, { recursive: true });
    } catch (error) {
        console.error('Error creating data directory:', error);
    }
}

// Initialize data files
async function initDataFiles() {
    await ensureDataDir();
    try {
        await fs.access(EMAILS_FILE);
    } catch {
        await fs.writeFile(EMAILS_FILE, JSON.stringify([], null, 2));
    }
    try {
        await fs.access(EVENTS_FILE);
    } catch {
        await fs.writeFile(EVENTS_FILE, JSON.stringify([], null, 2));
    }
}

// Hash email for privacy
function hashEmail(email) {
    return crypto.createHash('sha256').update(email.toLowerCase().trim()).digest('hex');
}

// Generate event ID
function generateEventId() {
    return 'evt_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
}

// Send event to TikTok Events API
async function sendToTikTokEventsAPI(eventData) {
    if (!TIKTOK_ACCESS_TOKEN) {
        console.warn('TikTok Access Token not configured. Skipping Events API call.');
        return null;
    }

    try {
        const payload = {
            event: eventData.event,
            event_id: eventData.event_id || generateEventId(),
            timestamp: eventData.timestamp || new Date().toISOString(),
            properties: {
                ...eventData.properties,
                // Add standard properties
                contents: [],
                content_type: eventData.properties?.content_type || 'web',
                currency: eventData.properties?.currency || 'USD',
                value: eventData.properties?.value || 0
            },
            context: {
                page: eventData.context?.page || {},
                user: {
                    external_id: eventData.properties?.email ? hashEmail(eventData.properties.email) : undefined,
                    phone_number: eventData.properties?.phone ? hashEmail(eventData.properties.phone) : undefined
                },
                user_agent: eventData.context?.user_agent || '',
                ip: eventData.context?.ip || ''
            }
        };

        // Map custom events to TikTok standard events
        const eventMapping = {
            'FollowButtonClick': 'ClickButton',
            'EmailSignup': 'CompleteRegistration',
            'PageEngagement': 'StayTime'
        };

        const tiktokEvent = eventMapping[eventData.event] || 'CustomEvent';
        payload.event = tiktokEvent;

        const response = await fetch(TIKTOK_EVENTS_API_URL, {
            method: 'POST',
            headers: {
                'Access-Token': TIKTOK_ACCESS_TOKEN,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                pixel_code: TIKTOK_PIXEL_ID,
                event: tiktokEvent,
                event_id: payload.event_id,
                timestamp: payload.timestamp,
                properties: payload.properties,
                context: payload.context,
                partner_name: 'tiktok'
            })
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('TikTok Events API error:', response.status, errorText);
            return null;
        }

        const result = await response.json();
        console.log('TikTok Events API success:', result);
        return result;

    } catch (error) {
        console.error('Error sending to TikTok Events API:', error);
        return null;
    }
}

// Routes

// Health check
app.get('/health', (req, res) => {
    res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Email subscription endpoint
app.post('/api/subscribe', async (req, res) => {
    try {
        const { email } = req.body;

        if (!email || !email.includes('@')) {
            return res.status(400).json({ error: 'Valid email required' });
        }

        // Read existing emails
        const emailsData = JSON.parse(await fs.readFile(EMAILS_FILE, 'utf8'));
        
        // Check if email already exists
        const exists = emailsData.some(e => e.email.toLowerCase() === email.toLowerCase());
        
        if (!exists) {
            emailsData.push({
                email: email,
                hashed_email: hashEmail(email),
                timestamp: new Date().toISOString(),
                source: 'tiktok_landing_page'
            });

            await fs.writeFile(EMAILS_FILE, JSON.stringify(emailsData, null, 2));
        }

        // Track conversion event
        const eventData = {
            event: 'EmailSignup',
            event_id: generateEventId(),
            timestamp: new Date().toISOString(),
            properties: {
                content_type: 'email_signup',
                email: email,
                value: 1,
                currency: 'USD'
            },
            context: {
                page: {
                    url: req.headers.referer || '',
                },
                user_agent: req.headers['user-agent'] || '',
                ip: req.ip || req.connection.remoteAddress
            }
        };

        // Send to TikTok Events API
        await sendToTikTokEventsAPI(eventData);

        // Store event
        const eventsData = JSON.parse(await fs.readFile(EVENTS_FILE, 'utf8'));
        eventsData.push(eventData);
        await fs.writeFile(EVENTS_FILE, JSON.stringify(eventsData, null, 2));

        res.json({ success: true, message: 'Email subscribed successfully' });

    } catch (error) {
        console.error('Subscribe error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// TikTok Events API endpoint (client-side calls this)
app.post('/api/tiktok-events', async (req, res) => {
    try {
        const eventData = req.body;

        // Send to TikTok Events API
        const result = await sendToTikTokEventsAPI(eventData);

        // Store event locally
        const eventsData = JSON.parse(await fs.readFile(EVENTS_FILE, 'utf8'));
        eventsData.push({
            ...eventData,
            sent_to_tiktok: result !== null,
            timestamp: new Date().toISOString()
        });
        await fs.writeFile(EVENTS_FILE, JSON.stringify(eventsData, null, 2));

        res.json({ success: true, sent_to_tiktok: result !== null });

    } catch (error) {
        console.error('TikTok events error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Export emails for lookalike audience (CSV format for TikTok)
app.get('/api/export/lookalike', async (req, res) => {
    try {
        const emailsData = JSON.parse(await fs.readFile(EMAILS_FILE, 'utf8'));
        
        // TikTok requires specific format for lookalike audiences
        // Format: email (hashed) or phone number
        const csvRows = emailsData.map(e => e.hashed_email);
        
        res.setHeader('Content-Type', 'text/csv');
        res.setHeader('Content-Disposition', 'attachment; filename="tiktok_lookalike_audience.csv"');
        res.send(csvRows.join('\n'));

    } catch (error) {
        console.error('Export error:', error);
        res.status(500).json({ error: 'Export failed' });
    }
});

// Get statistics
app.get('/api/stats', async (req, res) => {
    try {
        const emailsData = JSON.parse(await fs.readFile(EMAILS_FILE, 'utf8'));
        const eventsData = JSON.parse(await fs.readFile(EVENTS_FILE, 'utf8'));

        const stats = {
            total_emails: emailsData.length,
            total_events: eventsData.length,
            events_by_type: {},
            latest_emails: emailsData.slice(-10).reverse(),
            latest_events: eventsData.slice(-10).reverse()
        };

        eventsData.forEach(event => {
            stats.events_by_type[event.event] = (stats.events_by_type[event.event] || 0) + 1;
        });

        res.json(stats);

    } catch (error) {
        console.error('Stats error:', error);
        res.status(500).json({ error: 'Failed to get stats' });
    }
});

// Initialize and start server
async function start() {
    await initDataFiles();
    
    app.listen(PORT, () => {
        console.log(`🚀 TikTok Landing Page Server running on http://localhost:${PORT}`);
        console.log(`📊 Health check: http://localhost:${PORT}/health`);
        console.log(`📈 Stats: http://localhost:${PORT}/api/stats`);
        console.log(`📥 Export lookalike: http://localhost:${PORT}/api/export/lookalike`);
        console.log(`\n⚠️  Make sure to set environment variables:`);
        console.log(`   TIKTOK_PIXEL_ID=your_pixel_id`);
        console.log(`   TIKTOK_ACCESS_TOKEN=your_access_token`);
    });
}

start().catch(console.error);

