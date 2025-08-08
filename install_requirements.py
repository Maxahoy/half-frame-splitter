# install_requirements.py
import subprocess
import sys
import os

def ensure_dependencies():
    """
    Installs all dependencies listed in requirements.txt if they are not already installed.
    """
    requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if not os.path.exists(requirements_file):
        print("requirements.txt not found. No dependencies installed.")
        return

    try:
        print("Installing requirements.txt packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)
