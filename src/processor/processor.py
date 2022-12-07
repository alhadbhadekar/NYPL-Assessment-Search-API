from src.dataretriever.dataretriever import dataretriever
from src.formatter.formatter import formatter
from src.constants.http_status_codes import HTTP_200_OK

def processor(text: str):
    response = {
        'result': []
    }
    retrieved_data, status_code = dataretriever(text)
    if status_code != HTTP_200_OK:
        return response, status_code
    
    if retrieved_data is None:
        return response, status_code
    
    response = formatter(response, retrieved_data)
    return response, status_code