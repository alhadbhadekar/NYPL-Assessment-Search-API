import validators

def formatter(response, retrieved_data):
    for item in retrieved_data:
        new_item = {}
        if 'apiItemDetailURL' in item:
            if validators.url(item['apiItemDetailURL']):
                new_item['ItemDetailURL'] = item['apiItemDetailURL']
            else:
                new_item['ItemDetailURL'] = None
            
        if 'apiItemURL' in item:
            if validators.url(item['apiItemURL']):
                new_item['ItemURL'] = item['apiItemURL']
            else:
                new_item['ItemURL'] = None
        if 'dateDigitized' in item:
            new_item['Digitized Date'] = item['dateDigitized']
        if 'imageID' in item:
            new_item['ImageId'] = item['imageID']
        if 'itemLink' in item:
            new_item['Link'] = item['itemLink']
        if 'title' in item:
            new_item['Title'] = item['title']
        if 'typeOfResource' in item:
            new_item['TypeOfResource'] = item['typeOfResource']

        response['result'].append(new_item)

    return response