#!/bin/bash

# GitHub Repository Setup Script for Rick Roll Hello World
# Run this script to initialize and push your project to GitHub

echo "🚀 Setting up GitHub Repository for Rick Roll Hello World"
echo "======================================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    echo "   Visit: https://git-scm.com/downloads"
    exit 1
fi

echo "✅ Git is available"

# Check if we're already in a git repository
if [ -d ".git" ]; then
    echo "✅ Already a Git repository"
else
    echo "📁 Initializing Git repository..."
    git init
fi

# Add all files (excluding sensitive ones)
echo "📦 Adding files to Git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "🎵 Initial commit: Rick Roll Hello World with dancing Rick Astley

Features:
- Animated 8-bit dancing Rick Astley GIF
- MIDI music playback with silence trimming
- Security-hardened dependencies
- Multiple sharing options (executable, setup script)
- Complete documentation

Never gonna give you up! 🎶"

echo ""
echo "✅ Local Git setup complete!"
echo ""
echo "📋 Next steps to create GitHub repository:"
echo "1. Go to https://github.com and create a new repository"
echo "2. Repository name suggestion: rickroll-hello-world"
echo "3. Don't initialize with README (we already have one)"
echo "4. After creating, run these commands:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "🎉 Then share the GitHub URL with your friends!"
echo ""
echo "🎵 Happy rickrolling! 🎵"
