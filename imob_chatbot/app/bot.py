from google.oauth2 import service_account
import google.auth.transport.requests
from config import config

def get_access_token():
    credentials = service_account.Credentials.from_service_account_file(
        config.SERVICE_ACCOUNT_FILE, scopes=config.SCOPES
    )
    request_auth = google.auth.transport.requests.Request()
    credentials.refresh(request_auth)
    return credentials.token