#!python
import os
import subprocess
import sys

# ===================================================
# Run script for SDL executable
# ===================================================

# Top-level project directory (one level up from ./scripts)
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Build configuration: Release by default
CONFIG = "Release"

# Path to the executable
BIN_DIR = os.path.join(PROJECT_DIR, "build", "bin", CONFIG)
EXECUTABLE_NAME = "sdl_basic.exe"
EXECUTABLE_PATH = os.path.join(BIN_DIR, EXECUTABLE_NAME)

def main():
    # Check if executable exists
    if not os.path.exists(EXECUTABLE_PATH):
        print(f"Error: Executable not found at {EXECUTABLE_PATH}")
        print("Make sure you have built the project first.")
        sys.exit(1)

    # Run the executable
    try:
        print(f"Running {EXECUTABLE_NAME}...")
        subprocess.run([EXECUTABLE_PATH], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
