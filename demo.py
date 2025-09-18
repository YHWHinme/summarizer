#!/usr/bin/env python3
"""
Demo script showing how to use the video summarizer
This script demonstrates the workflow without requiring actual video files
"""

import os
from pathlib import Path

def show_usage_examples():
    """Display usage examples for the video summarizer"""

    print("🎥 Video Summarizer - Usage Examples")
    print("=" * 50)

    print("\n📋 Prerequisites:")
    print("1. Install dependencies: uv sync")
    print("2. Get Gemini API key from: https://makersuite.google.com/app/apikey")
    print("3. Set environment variable: export GEMINI_API_KEY=your_key_here")

    print("\n🚀 Basic Usage Examples:")
    print()

    print("1️⃣ Basic video summarization:")
    print("   python summarize_video.py video.mp4 --api-key $GEMINI_API_KEY")
    print()

    print("2️⃣ Save summary to file:")
    print("   python summarize_video.py video.mp4 --api-key $GEMINI_API_KEY --output summary.md")
    print()

    print("3️⃣ Enhanced summarization with transcription:")
    print("   # First transcribe")
    print("   python tts.py video.mp4 --output transcript.json")
    print("   # Then summarize with transcript")
    print("   python summarize_video.py video.mp4 --api-key $GEMINI_API_KEY --transcript transcript.json")
    print()

    print("4️⃣ Use different Whisper model sizes:")
    print("   python tts.py video.mp4 --model tiny --output transcript.json    # Fastest")
    print("   python tts.py video.mp4 --model base --output transcript.json    # Balanced")
    print("   python tts.py video.mp4 --model large --output transcript.json   # Most accurate")
    print()

    print("5️⃣ Custom summarization prompt:")
    print("   python summarize_video.py video.mp4 --api-key $GEMINI_API_KEY \\")
    print("     --custom-prompt 'Focus on technical details and code examples'")
    print()

def show_project_structure():
    """Show the project file structure"""
    print("\n📁 Project Structure:")
    print("=" * 30)

    files = [
        "📄 pyproject.toml     # Project configuration with dependencies",
        "📄 requirements.txt   # Alternative dependency specification",
        "📄 README.md          # Comprehensive documentation",
        "📄 summarize_video.py # Main Gemini summarization script",
        "📄 tts.py            # Whisper transcription module",
        "📄 test_installation.py # Dependency verification script",
        "📄 demo.py           # This demo script",
        "📄 main.py           # Simple entry point"
    ]

    for file in files:
        print(f"   {file}")

def show_workflow():
    """Show the complete workflow"""
    print("\n🔄 Complete Workflow:")
    print("=" * 25)

    steps = [
        "1. Install dependencies: uv sync",
        "2. Get Gemini API key from Google AI Studio",
        "3. Set API key: export GEMINI_API_KEY=your_key",
        "4. Test installation: python test_installation.py",
        "5. Transcribe video (optional): python tts.py video.mp4 --output transcript.json",
        "6. Summarize video: python summarize_video.py video.mp4 --api-key $GEMINI_API_KEY",
        "7. View results in terminal or saved file"
    ]

    for step in enumerate(steps, 1):
        print(f"   {step[0]}. {step[1]}")

def main():
    """Main demo function"""
    print("🎬 Welcome to the Video Summarizer Demo!")
    print("This tool combines Google's Gemini AI with Faster-Whisper for powerful video analysis.")
    print()

    show_project_structure()
    show_usage_examples()
    show_workflow()

    print("\n✨ Ready to get started?")
    print("Run: uv sync")
    print("Then: python test_installation.py")
    print()
    print("Happy summarizing! 🚀")

if __name__ == "__main__":
    main()