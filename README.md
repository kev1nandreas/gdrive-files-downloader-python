# Python Google Drive Files Downloader

## Description

This is a script that connects directly to Google Drive using a Client ID and Client Secret for authentication. It is made to download multiple files directly from Google Drive without using the Drive platform. Ideal for automation tasks, it enables seamless downloads without manual authentication and supports secure OAuth 2.0 authentication, making it perfect for retrieving large files, backups, or shared documents efficiently.

## Requirements

To use this script, u need to install some requirements package by using this command.

```
npm install -r requirements.txt
```

## How to Use

1. Get your Google Drive Client ID, Project ID, and Client Secret. This is a recommended guide for [how to get it](https://support.google.com/workspacemigrate/answer/9222992?hl=ID)

2. Configure the `client_id`, `project_id`, and `client_secret` in `client_secret_example.json`. You can change the other variables if it is needed.

    ```json
    {
    "installed": {
        "client_id": "your_client_id",
        "project_id": "your_project_id",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "your_client_secret",
        "redirect_uris": ["http://localhost"]
    }
    }
    ```

3. Change the `CLIENT_SECRET_FILE` in `main.py` (only if you rename the .json file name)

    ```python
    CLIENT_SECRET_FILE = "client_secret_example.json"
    ```

4. Configure these variables in `main.py`.

    ```python
    CSV_FILE_NAME = "template.csv"
    COL_BEGIN = 0
    FILE_HAS_HEADER = False
    FOLDER_NAME = "Your Folder Name"
    ```

    - `CSV_FILE_NAME` is the name of the file that contains the links.
    - `ROW_BEGIN` specifies the column that contains the links. A value of 0 corresponds to the first column, 1 to the second, and so on. Only one row can be processed at a time while running the script.
    - `FILE_HAS_HEADER` specifies whether your csv file has header.
    - `FOLDER_NAME` is the name of the output folder containing all the downloaded files.

5. Run the program using this command.

    ```
    python main.py
    ```

6. Allow all the authorization requests.

