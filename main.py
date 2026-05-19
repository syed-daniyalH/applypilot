import os
import subprocess
import sys
import time
import urllib.error
import urllib.request


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SERVER_URL = "http://127.0.0.1:5000/applied-jobs"


def is_server_ready(url: str = SERVER_URL) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=1) as response:
            return 200 <= response.status < 300
    except (urllib.error.URLError, TimeoutError):
        return False


def start_dashboard() -> subprocess.Popen | None:
    if is_server_ready():
        print("Dashboard is already running on http://127.0.0.1:5000")
        return None

    env = os.environ.copy()
    env.setdefault("FLASK_DEBUG", "0")

    dashboard_process = subprocess.Popen(
        [sys.executable, "app.py"],
        cwd=PROJECT_ROOT,
        env=env,
    )

    for _ in range(40):
        if is_server_ready():
            print("Dashboard started on http://127.0.0.1:5000")
            return dashboard_process
        if dashboard_process.poll() is not None:
            raise RuntimeError("Dashboard exited before it became ready.")
        time.sleep(0.5)

    dashboard_process.terminate()
    raise TimeoutError("Dashboard did not become ready in time.")


def run_bot() -> int:
    print("Starting LinkedIn bot...")
    completed = subprocess.run(
        [sys.executable, "runAiBot.py"],
        cwd=PROJECT_ROOT,
    )
    return completed.returncode


def stop_dashboard(dashboard_process: subprocess.Popen | None) -> None:
    if dashboard_process is None or dashboard_process.poll() is not None:
        return

    dashboard_process.terminate()
    try:
        dashboard_process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        dashboard_process.kill()
        dashboard_process.wait(timeout=5)


def main() -> int:
    dashboard_process = None
    try:
        dashboard_process = start_dashboard()
        return run_bot()
    except KeyboardInterrupt:
        print("\nLauncher stopped by user.")
        return 130
    except Exception as exc:
        print(f"Failed to launch project: {exc}")
        return 1
    finally:
        stop_dashboard(dashboard_process)


if __name__ == "__main__":
    raise SystemExit(main())
