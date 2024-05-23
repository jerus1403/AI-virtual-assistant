import sys
import signal


def signal_handler(sig, frame):
    print("Exiting gracefully")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
