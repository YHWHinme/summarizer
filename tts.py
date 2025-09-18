#!/usr/bin/env python3
"""
Video Transcription Module using Faster-Whisper
Transcribes MP4 files to text with timestamps and metadata.
"""

from faster_whisper import WhisperModel
from pathlib import Path
import json
import sys
from typing import Dict, List, Optional

class VideoTranscriber:
    def __init__(self, model_size: str = "medium", device: str = "auto", compute_type: str = "float16"):
        """
        Initialize the Whisper model
        Args:
            model_size: Model size (tiny, base, small, medium, large)
            device: Device to run on (auto, cpu, cuda)
            compute_type: Precision (float16, float32, int8)
        """
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)

    def transcribe_video(self, video_path: str, language: Optional[str] = None) -> Dict:
        """
        Transcribe video file to text with timestamps
        """
        if not Path(video_path).exists():
            raise FileNotFoundError(f"Video file not found: {video_path}")

        # Transcribe with optional language specification
        segments, info = self.model.transcribe(
            video_path,
            language=language,
            vad_filter=True,  # Filter out non-speech
            vad_parameters=dict(threshold=0.5, min_speech_duration_ms=250)
        )

        transcription = []
        for segment in segments:
            transcription.append({
                'start': round(segment.start, 2),
                'end': round(segment.end, 2),
                'text': segment.text.strip(),
                'confidence': round(segment.avg_logprob, 3) if hasattr(segment, 'avg_logprob') else None
            })

        return {
            'language': info.language,
            'language_probability': round(info.language_probability, 3),
            'duration': info.duration,
            'transcription': transcription,
            'full_text': ' '.join([seg['text'] for seg in transcription]).strip()
        }

    def save_transcription(self, result: Dict, output_path: str):
        """Save transcription to JSON file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

def main():
    """CLI interface for transcription"""
    if len(sys.argv) < 2:
        print("Usage: python tts.py <video_path> [--model MODEL] [--output OUTPUT]")
        print("Example: python tts.py video.mp4 --model base --output transcript.json")
        sys.exit(1)

    video_path = sys.argv[1]
    model_size = "medium"  # default
    output_path = None

    # Parse additional arguments
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--model" and i + 1 < len(args):
            model_size = args[i + 1]
            i += 2
        elif args[i] == "--output" and i + 1 < len(args):
            output_path = args[i + 1]
            i += 2
        else:
            i += 1

    try:
        transcriber = VideoTranscriber(model_size=model_size)
        result = transcriber.transcribe_video(video_path)

        if output_path:
            transcriber.save_transcription(result, output_path)
            print(f"Transcription saved to: {output_path}")
        else:
            print(f"Language: {result['language']} ({result['language_probability']})")
            print(f"Duration: {result['duration']:.1f}s")
            print(f"\nFull Text:\n{result['full_text']}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()