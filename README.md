# Video Summarizer

A powerful CLI tool that summarizes MP4 video files using Google's Gemini multimodal AI, with optional transcription support using Faster-Whisper.

## Features

- 🎥 **Direct Video Analysis**: Uses Gemini's native video understanding capabilities
- 🎙️ **Optional Transcription**: Integrates Faster-Whisper for enhanced accuracy
- 📝 **Structured Summaries**: Markdown-formatted output with key insights
- ⚡ **GPU Acceleration**: Supports CUDA for faster processing
- 🛠️ **CLI Interface**: Clean command-line interface with Click

## Installation

### Using uv (recommended)
```bash
uv add faster-whisper torch google-generativeai click
```

### Using pip
```bash
pip install faster-whisper torch google-generativeai click
```

## Usage

### 1. Get a Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Set it as an environment variable: `export GEMINI_API_KEY=your_key_here`

### 2. Basic Video Summarization
```bash
python summarize_video.py video.mp4 --api-key YOUR_API_KEY
```

### 3. Enhanced Summarization with Transcription
```bash
# First, transcribe the video
python tts.py video.mp4 --output transcript.json

# Then summarize with transcript
python summarize_video.py video.mp4 --api-key YOUR_API_KEY --transcript transcript.json
```

### 4. Save Summary to File
```bash
python summarize_video.py video.mp4 --api-key YOUR_API_KEY --output summary.md
```

## Command Options

### summarize_video.py
- `video_path`: Path to MP4 file (required)
- `--api-key`: Google Gemini API key (required)
- `--transcript`: Optional JSON transcript file for enhanced summarization
- `--output`: Optional output file path
- `--custom-prompt`: Optional custom summarization prompt

### tts.py
- `video_path`: Path to MP4 file (required)
- `--model`: Whisper model size (tiny, base, small, medium, large) [default: medium]
- `--output`: Optional JSON output file path

## Model Options

### Whisper Models (for transcription)
- `tiny`: Fastest, ~1GB VRAM
- `base`: Good balance, ~1GB VRAM
- `small`: Better accuracy, ~2GB VRAM
- `medium`: High accuracy, ~5GB VRAM (default)
- `large`: Best accuracy, ~10GB VRAM

## Requirements

- Python 3.9+
- FFmpeg (for audio processing)
- NVIDIA GPU (optional, for CUDA acceleration)

## Output Format

The tool generates structured markdown summaries including:
- Video duration and visual elements
- Key scenes and audio content
- Main takeaways and insights
- Overall summary

## Examples

### Basic Usage
```bash
$ python summarize_video.py demo.mp4 --api-key $GEMINI_API_KEY

==================================================
VIDEO SUMMARY
==================================================

## Video Summary

**Duration**: 2:34
**Visual Elements**: Conference room with presentation screen, speaker at podium
**Audio Content**: Clear speech about AI technology advancements
**Key Takeaways**:
- AI is transforming industries
- Machine learning adoption is accelerating
- Future applications in healthcare and finance
**Overall Summary**: This presentation discusses current AI trends and future applications, highlighting the transformative potential of machine learning technologies.
```

### With Transcription
```bash
$ python tts.py demo.mp4 --output transcript.json
$ python summarize_video.py demo.mp4 --api-key YOUR_API_KEY --transcript transcript.json --output summary.md
```

## Troubleshooting

### Common Issues
1. **API Key Error**: Ensure your Gemini API key is valid and has quota
2. **CUDA Error**: Install CUDA toolkit if using GPU acceleration
3. **Memory Error**: Use smaller Whisper models for limited RAM
4. **Video Format**: Ensure MP4 files are properly encoded

### Performance Tips
- Use GPU acceleration for faster processing
- Choose appropriate Whisper model size based on your hardware
- For long videos, consider transcribing first for better accuracy

## License

MIT License - see LICENSE file for details.