#!/usr/bin/env python3
"""
Test script to verify all dependencies are properly installed
"""

def test_imports():
    """Test that all required packages can be imported"""
    try:
        import faster_whisper
        print("✅ faster-whisper imported successfully")
    except ImportError as e:
        print(f"❌ faster-whisper import failed: {e}")

    try:
        import torch
        print(f"✅ torch imported successfully (version: {torch.__version__})")
    except ImportError as e:
        print(f"❌ torch import failed: {e}")

    try:
        import google.generativeai as genai
        print("✅ google-generativeai imported successfully")
    except ImportError as e:
        print(f"❌ google-generativeai import failed: {e}")

    try:
        import click
        print(f"✅ click imported successfully (version: {click.__version__})")
    except ImportError as e:
        print(f"❌ click import failed: {e}")

    try:
        import numpy as np
        print(f"✅ numpy imported successfully (version: {np.__version__})")
    except ImportError as e:
        print(f"❌ numpy import failed: {e}")

if __name__ == "__main__":
    print("Testing package installations...")
    print("=" * 50)
    test_imports()
    print("=" * 50)
    print("Installation test complete!")