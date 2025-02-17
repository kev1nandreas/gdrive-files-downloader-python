import os
import io
import csv
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENT_SECRET_FILE = "client_secret_example.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

############ Please fill this segment! ############

CSV_FILE_NAME = "template.csv"
COL_BEGIN = 0
FILE_HAS_HEADER = False
FOLDER_NAME = "Your Folder Name"

###################################################

files_id = []

with open(CSV_FILE_NAME) as csvfile:
    csv_reader = csv.reader(csvfile)
    if FILE_HAS_HEADER:
        next(csv_reader)
    
    for row in csv_reader:
        url = row[COL_BEGIN]
        file_id = url.split("=")[1]
        files_id.append(file_id)

os.makedirs(FOLDER_NAME, exist_ok=True)

for index, file_id in enumerate(files_id):
    # Get the metadata of the file
    file_metadata = service.files().get(fileId=file_id).execute()
    file_name = file_metadata['name']
    
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()

    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False

    # Download process
    while not done:
        status, done = downloader.next_chunk()
        print(f'Download progress {status.progress() * 100}%')
    
    fh.seek(0)

    # Determine the file extension from the file name
    file_extension = os.path.splitext(file_name)[1]
    
    # Specify the file path where you want to save the downloaded file
    save_path = os.path.join(os.getcwd(), FOLDER_NAME, f"downloaded_file_{index+1}{file_extension}")

    # Write the contents of the byte stream to a file
    with open(save_path, "wb") as f:
        f.write(fh.read())
    
    print(f"File downloaded and saved to: {save_path}")
