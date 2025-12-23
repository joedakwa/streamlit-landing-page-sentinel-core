#!/bin/bash

# Quick Deploy Script for TikTok Landing Page
# Usage: ./deploy.sh [tiktok_username] [pixel_id]

TIKTOK_USERNAME=${1:-"YOUR_USERNAME"}
PIXEL_ID=${2:-"YOUR_PIXEL_ID"}

echo "🚀 Deploying TikTok Landing Page..."
echo "Username: $TIKTOK_USERNAME"
echo "Pixel ID: $PIXEL_ID"

# Update index.html with username and pixel ID
sed -i "s/YOUR_USERNAME/$TIKTOK_USERNAME/g" index.html
sed -i "s/YOUR_PIXEL_ID/$PIXEL_ID/g" index.html

echo "✅ Files updated!"
echo ""
echo "Next steps:"
echo "1. Deploy to Vercel: vercel --prod"
echo "2. Or deploy to Netlify: drag index.html to netlify.com/drop"
echo "3. Or use GitHub Pages"

