from pathlib import Path
from zipfile import ZipFile

import requests

resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

# Download and save the zip file
all_files = requests.get("https://zenodo.org/api/records/4965431/files-archive")

all_files_path = folder_path / "all_files.zip"
with open(all_files_path, "wb") as file:
    file.write(all_files.content)

# Extract the zip file
with ZipFile(all_files_path, "r") as zip_ref:
    zip_ref.extractall(folder_path)
