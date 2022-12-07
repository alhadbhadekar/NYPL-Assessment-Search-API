import requests
import os
import json
from src.constants.http_status_codes import HTTP_500_INTERNAL_SERVER_ERROR

def dataretriever(text: str):

    url = os.environ.get("NYPL_URL")+"?q={}&publicDomainOnly=true".format(text)

    payload={}
    headers = {
        'Authorization': 'Token token="{}"'.format(os.environ.get("NYPL_AUTHORIZATION_TOKEN"))
    }
    try:
        response = requests.get(url, headers=headers, data=payload)
    except requests.exceptions.HTTPError as e:
        return None, HTTP_500_INTERNAL_SERVER_ERROR
    
    if response.status_code != 200:
        return None, response.status_code
    
    response_json = json.loads(response.text)

    if int(response_json['nyplAPI']['response']['numResults']) <= 0:
        return None, response.status_code
    
    return response_json['nyplAPI']['response']['result'], response.status_code
