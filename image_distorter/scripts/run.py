#!python
import os
import subprocess
import sys

# ===================================================
# Run executable from build/bin folder with config selection
# ===================================================

# Top-level project directory (one level up from ./scripts)
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Default configuration
DEFAULT_CONFIG = "Release"

def get_config():
    """Prompt user for configuration or use default."""
    if len(sys.argv) > 1 and sys.argv[1] in ("Release", "Debug"):
        config = sys.argv[1]
        extra_args = sys.argv[2:]
    else:
        config = DEFAULT_CONFIG
        extra_args = sys.argv[1:]
    return config, extra_args

def get_bin_dir(config):
    """Return the bin directory for the given configuration."""
    return os.path.join(PROJECT_DIR, "bin", config)

def list_executables(bin_dir):
    """List all executable files in the bin directory."""
    if not os.path.exists(bin_dir):
        return []
    executables = []
    for f in os.listdir(bin_dir):
        path = os.path.join(bin_dir, f)
        if os.path.isfile(path):
            if os.name == "nt" and f.endswith(".exe"):
                executables.append(f)
            elif os.name != "nt" and os.access(path, os.X_OK):
                executables.append(f)
    return executables

def choose_executable(executables):
    """Prompt user to choose an executable if multiple exist."""
    if len(executables) == 1:
        return executables[0]
    print("Multiple executables found:")
    for i, exe in enumerate(executables):
        print(f"{i+1}: {exe}")
    choice = input(f"Select executable [1-{len(executables)}]: ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(executables):
            return executables[idx]
    except ValueError:
        pass
    print("Invalid choice, defaulting to first executable.")
    return executables[0]

def run_executable(bin_dir, exe_name, args):
    exe_path = os.path.join(bin_dir, exe_name)
    print(f"Running: {exe_path} {' '.join(args)}")
    try:
        subprocess.check_call([exe_path] + args)
    except subprocess.CalledProcessError as e:
        print(f"Error running {exe_name}: {e}")
        sys.exit(1)

def main():
    config, extra_args = get_config()
    bin_dir = get_bin_dir(config)
    if not os.path.exists(bin_dir):
        print(f"Error: {bin_dir} does not exist.")
        sys.exit(1)

    executables = list_executables(bin_dir)
    if not executables:
        print(f"No executables found in {bin_dir}")
        sys.exit(1)

    exe_to_run = choose_executable(executables)
    run_executable(bin_dir, exe_to_run, extra_args)

if __name__ == "__main__":
    main()
