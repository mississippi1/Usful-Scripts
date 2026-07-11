import os
import requests
from pathlib import Path

# Create the download folder in Downloads directory
downloads_folder = Path.home() / "Downloads" / "downloaded_ex"
downloads_folder.mkdir(parents=True, exist_ok=True)

# Base URL
base_url = "https://mvcomp2-w2324.tristanbereau.com/exercises/exercise_{}.pdf"

# Iterate over numbers 0 to 30
for number in range(31):  # 0 to 30 inclusive
    url = base_url.format(f"{number:02d}")
    file_path = downloads_folder / f"exercise_{number:02d}.pdf"
    
    try:
        print(f"Attempting to download exercise {number:02d}... ({url})", end=" ")
        
        # Send GET request
        response = requests.get(url, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the file
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"✓ Downloaded successfully")
        elif response.status_code == 404:
            print(f"✗ File not found (404)")
        else:
            print(f"✗ Failed with status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Error: {e}")

print(f"\nDownload complete! Files saved to: {downloads_folder}")
