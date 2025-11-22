#!python
import os
import shutil
import subprocess
import sys
import platform

# ===================================================
# Build script for CUDA + CMake using GCC/MinGW on Windows or GCC/Clang on Linux
# ===================================================

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG = "Release"
BIN_DIR_NAME = "bin"

def run_command(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.check_call(cmd, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def detect_platform():
    system = platform.system()
    if system == "Windows":
        # Use MinGW-w64 GCC on Windows
        compiler_info = {
            "generator": "MinGW Makefiles",
            "arch": None,
            "c_compiler": "gcc",
            "cxx_compiler": "g++",
            "build_dir": os.path.join(PROJECT_DIR, "build")
        }
    else:
        # Linux / macOS
        compiler_info = {
            "generator": "Ninja",
            "arch": None,
            "c_compiler": "gcc",
            "cxx_compiler": "g++",
            "build_dir": os.path.join(PROJECT_DIR, "build")
        }
    return compiler_info

def main():
    compiler_info = detect_platform()
    BUILD_DIR = compiler_info["build_dir"]
    BIN_DIR = os.path.join(BIN_DIR_NAME, CONFIG)

    if os.path.exists(BUILD_DIR):
        print(f"Removing existing build directory: {BUILD_DIR}")
        shutil.rmtree(BUILD_DIR)

    os.makedirs(BIN_DIR, exist_ok=True)

    # Configure CMake
    cmake_config_cmd = [
        "cmake",
        f"-S{PROJECT_DIR}",
        f"-B{BUILD_DIR}",
        f"-G{compiler_info['generator']}",
        f"-DCMAKE_BUILD_TYPE={CONFIG}",
        f"-DCMAKE_RUNTIME_OUTPUT_DIRECTORY={BIN_DIR}",
        f"-DCMAKE_C_COMPILER={compiler_info['c_compiler']}",
        f"-DCMAKE_CXX_COMPILER={compiler_info['cxx_compiler']}"
    ]

    run_command(cmake_config_cmd)

    # Build project
    cmake_build_cmd = [
        "cmake",
        "--build", BUILD_DIR,
        "--config", CONFIG,
        "--parallel"
    ]
    run_command(cmake_build_cmd)

    print(f"Build complete! Executable(s) in: {BIN_DIR}")

if __name__ == "__main__":
    main()
