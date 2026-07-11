import os
import requests
from pathlib import Path

# Create the download folder in Downloads directory
downloads_folder = Path.home() / "Downloads" / "downloaded_mlph_sheets"
downloads_folder.mkdir(parents=True, exist_ok=True)

# Base URL - using raw.githubusercontent.com for direct file access
base_url = "https://raw.githubusercontent.com/sciai-lab/mlph-25w/main/sheet{}/sheet{}.pdf"

# Iterate over numbers 01 to 14
for number in range(1, 15):  # 1 to 14 inclusive
    number_str = f"{number:02d}"
    url = base_url.format(number_str, number_str)
    file_path = downloads_folder / f"sheet{number_str}.pdf"
    
    try:
        print(f"Attempting to download sheet {number_str}... ({url})", end=" ")
        
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
