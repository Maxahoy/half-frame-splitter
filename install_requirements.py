import sys
import subprocess
import importlib.metadata

REQUIRED_PACKAGES = [
    "opencv-python",
    "numpy",
    "pillow"
]

def install_package(package):
    """
    Install a single package using pip.
    """
    print(f"Installing missing package: {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def ensure_dependencies():
    """
    Ensure all required packages are installed.
    Returns True if any packages were installed, otherwise False.
    """
    installed_any = False
    for package in REQUIRED_PACKAGES:
        try:
            importlib.metadata.version(package)
            print(f"Package {package} was found; no need to install!")
        except importlib.metadata.PackageNotFoundError:
            install_package(package)
            installed_any = True
    return installed_any
