import os
import sys
from install_requirements import ensure_dependencies

if __name__ == "__main__":
    # Step 1: Ensure dependencies
    installed_new = ensure_dependencies()

    # Step 2: Restart if new packages were installed
    if installed_new:
        print("\nNew packages installed. Restarting script...\n")
        os.execv(sys.executable, [sys.executable] + sys.argv)

    # Step 3: Import and run the actual program
    import splitter
    splitter.run()  # We'll assume splitter.py has a run() function
