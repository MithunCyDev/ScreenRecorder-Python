"""Build script for creating the executable."""
import os
import subprocess
import sys
import shutil
from pathlib import Path

def get_python_executable():
    """Get the correct Python executable path."""
    if sys.platform == "win32":
        python_exe = os.path.join(sys.prefix, "python.exe")
        if not os.path.exists(python_exe):
            python_exe = sys.executable
        return python_exe
    return sys.executable

def install_requirements():
    """Install required packages for building."""
    python_exe = get_python_executable()
    print("Installing build requirements...")
    subprocess.run(
        [python_exe, "-m", "pip", "install", "-r", "requirements_build.txt"],
        check=True
    )

def clean_build_dirs():
    """Clean previous build directories."""
    for dir_name in ["build", "dist"]:
        if os.path.exists(dir_name):
            print(f"Cleaning {dir_name} directory...")
            shutil.rmtree(dir_name)

def run_pyinstaller():
    """Run PyInstaller with the spec file."""
    print("Building executable...")
    pyinstaller_path = shutil.which("pyinstaller")
    if not pyinstaller_path:
        print("PyInstaller not found in PATH. Trying to find it in Python scripts...")
        scripts_dir = Path(sys.prefix) / "Scripts"
        pyinstaller_path = str(scripts_dir / "pyinstaller.exe")
        if not os.path.exists(pyinstaller_path):
            raise FileNotFoundError("Could not find PyInstaller executable")

    subprocess.run(
        [pyinstaller_path, "build_config.spec", "--clean"],
        check=True
    )

def main():
    """Main build function."""
    try:
        # Create dist directory if it doesn't exist
        os.makedirs("dist", exist_ok=True)
        
        # Install requirements
        install_requirements()
        
        # Clean previous builds
        clean_build_dirs()
        
        # Run PyInstaller
        run_pyinstaller()
        
        print("\nBuild complete! Executable can be found in the 'dist' folder.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during build process: {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()