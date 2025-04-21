import signal
import time

def handle_sigterm(signum, frame):
    print("📩 Got termination signal. Starting cleanup...")
    time.sleep(3)
    print("✅ Saved unsaved items to database (simulated)")
    time.sleep(3)
    print("🛑 Closed DB connection (simulated)")
    print("🚪 Exiting now.")
    exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)

print("✅ Python app started. Waiting...")

# Infinite loop
while True:
    time.sleep(1)
