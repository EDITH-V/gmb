import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import datetime


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    """
    Creates a service object for the specified API using the provided client secret file and scopes.

    Args:
        client_secret_file (str): The path to the client secret file.
        api_name (str): The name of the API.
        api_version (str): The version of the API.
        *scopes (str): Variable number of scopes required for the API.

    Returns:
        service: The service object for the specified API.

    Raises:
        Exception: If unable to connect to the API.

    """
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

CLIENT_SECRET_FILE = "client_secret.json" 
API_NAME = 'mybusinessbusinessinformation'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/business.manage']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
print(dir(service))
new_business = service.accounts().locations().create(body={
    "languageCode": "en-US",
    "storeCode": "storeCode123",
    "title": "storeName123",
    "websiteUri": "https://www.google.com",
    "categories":{
        "primaryCategory": {
            "name": "Shoe store123",
            "displayName": "Shoe store",
            }
    },
    "storefrontAddress": {
        "revision": 0,
        "regionCode": "US"
  }
}, parent="accounts/107696407368077692646")

#get the account id from the google mybusiness agency dashboard
list_business = service.accounts().locations().list(parent="accounts/107696407368077692646")
list_business.execute()

