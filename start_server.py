import subprocess

from torchvision import datasets
from torchvision import transforms
from pathlib import Path

import signal
import sys


python = Path(sys.executable).name

FILE_PATH = Path(__file__).resolve().parents[0].joinpath("siim_server.py")

call_alice = [
    python,
    FILE_PATH,
    "--port",
    "8777",
    "--id",
    "alice",
    "--host",
    "0.0.0.0",
    "--notebook",
    "parallel",
]

call_bob = [
    python,
    FILE_PATH,
    "--port",
    "8778",
    "--id",
    "bob",
    "--host",
    "0.0.0.0",
    "--notebook",
    "parallel",
]


call_testing = [
    python,
    FILE_PATH,
    "--port",
    "8780",
    "--id",
    "testing",
    "--testing",
    "--host",
    "0.0.0.0",
    "--notebook",
    "parallel",
]

print("Starting server for Alice")
process_alice = subprocess.Popen(call_alice)

print("Starting server for Bob")
process_bob = subprocess.Popen(call_bob)

print("Starting server for Testing")
process_testing = subprocess.Popen(call_testing)


def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    for p in [process_alice, process_bob, process_testing]:
        p.terminate()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

signal.pause()
