#!/usr/bin/env python3
"""
Video Summarization CLI using Google Gemini
Summarizes MP4 files using multimodal AI with optional transcript integration.
"""

import google.generativeai as genai
import click
from pathlib import Path
import json
from typing import Optional

class VideoSummarizer:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def summarize_video(self, video_path: str, custom_prompt: Optional[str] = None) -> str:
        """
        Summarize video using Gemini
        """
        if not Path(video_path).exists():
            raise FileNotFoundError(f"Video file not found: {video_path}")

        # Upload video file
        print("Uploading video to Gemini...")
        video_file = genai.upload_file(video_path)

        # Default summarization prompt
        if custom_prompt is None:
            custom_prompt = """
            You are an expert video content analyzer. Given this video, provide a brief, structured summary in markdown format with:

            ## Video Summary

            **Duration**: [estimated length]
            **Visual Elements**: Key scenes, objects, and visual themes
            **Audio Content**: Spoken words, sounds, and audio cues
            **Key Takeaways**: 3-5 main points or insights
            **Overall Summary**: 2-3 sentence overview of the video's purpose and content

            Keep the summary concise (under 300 words) and focus on the most important visual and audio information.
            """

        # Generate summary
        print("Generating summary...")
        response = self.model.generate_content([custom_prompt, video_file])

        return response.text

    def summarize_with_transcript(self, video_path: str, transcript_path: str) -> str:
        """
        Summarize video using both video and transcript
        """
        if not Path(transcript_path).exists():
            raise FileNotFoundError(f"Transcript file not found: {transcript_path}")

        # Load transcript
        with open(transcript_path, 'r', encoding='utf-8') as f:
            transcript_data = json.load(f)

        transcript_text = transcript_data.get('full_text', '')

        # Upload video
        video_file = genai.upload_file(video_path)

        prompt = f"""
        You have both a video file and its transcription. Provide a comprehensive summary that combines visual and audio information.

        TRANSCRIPT:
        {transcript_text}

        Please analyze the video and provide a structured summary in markdown format covering:
        - Visual content and key scenes
        - Audio/transcript highlights
        - Main themes and takeaways
        - Overall purpose of the video

        Keep the summary under 400 words.
        """

        response = self.model.generate_content([prompt, video_file])
        return response.text

@click.command()
@click.argument('video_path', type=click.Path(exists=True))
@click.option('--api-key', required=True, help='Google Gemini API key')
@click.option('--transcript', type=click.Path(exists=True), help='Optional transcript JSON file')
@click.option('--output', type=click.Path(), help='Output file for summary')
@click.option('--custom-prompt', help='Custom summarization prompt')
def main(video_path, api_key, transcript, output, custom_prompt):
    """Summarize video using Google Gemini"""
    try:
        summarizer = VideoSummarizer(api_key)

        if transcript:
            print("Using video + transcript for enhanced summarization...")
            summary = summarizer.summarize_with_transcript(video_path, transcript)
        else:
            print("Summarizing video directly...")
            summary = summarizer.summarize_video(video_path, custom_prompt)

        if output:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(summary)
            print(f"Summary saved to: {output}")
        else:
            print("\n" + "="*50)
            print("VIDEO SUMMARY")
            print("="*50)
            print(summary)

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        return 1

if __name__ == "__main__":
    main()