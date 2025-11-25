#!python
import os
import shutil
import subprocess
import sys

# ===================================================
# Build script for CUDA + CMake + MSVC using Python
# ===================================================

# Top-level project directory
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Build directory
BUILD_DIR = os.path.join(PROJECT_DIR, "build")

# Output folder for executables
BIN_DIR = os.path.join(BUILD_DIR, "bin")

# Visual Studio generator
GENERATOR = "Visual Studio 17 2022"
ARCH = "x64"
CONFIG = "Release"

def run_command(cmd, cwd=None):
    """Run a command and print its output."""
    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.check_call(cmd, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    # Remove old build directory if it exists
    if os.path.exists(BUILD_DIR):
        print("Removing existing build directory...")
        shutil.rmtree(BUILD_DIR)

    # Create build and bin directories
    os.makedirs(BIN_DIR, exist_ok=True)

    # Step 1: Configure CMake
    cmake_config_cmd = [
        "cmake",
        f"-G{GENERATOR}",
        f"-A{ARCH}",
        f"-DCMAKE_RUNTIME_OUTPUT_DIRECTORY={BIN_DIR}",
        PROJECT_DIR
    ]
    run_command(cmake_config_cmd, cwd=BUILD_DIR)

    # Step 2: Build the project in Release mode
    cmake_build_cmd = [
        "cmake",
        "--build", ".",
        "--config", CONFIG
    ]
    run_command(cmake_build_cmd, cwd=BUILD_DIR)

    print(f"Build complete! Executable(s) should be in: {BIN_DIR}")

if __name__ == "__main__":
    main()
