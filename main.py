import os
import sys
from install_requirements import ensure_dependencies

MAX_RESTARTS = 2

def get_restart_count():
    try:
        return int(os.environ.get("RESTART_COUNT", "0"))
    except ValueError:
        return 0

if __name__ == "__main__":
    restart_count = get_restart_count()

    # Step 1: Ensure dependencies
    installed_new = ensure_dependencies()

    # Step 2: Restart if new packages were installed and restart count not exceeded
    if installed_new and restart_count < MAX_RESTARTS:
        print(f"\nNew packages installed. Restarting script... (restart {restart_count + 1}/{MAX_RESTARTS})\n")
        # Increase restart count by 1 in environment variable and restart
        os.environ["RESTART_COUNT"] = str(restart_count + 1)
        os.execv(sys.executable, [sys.executable] + sys.argv)

    # Step 3: Import and run the actual program
    import splitter
    splitter.run()
