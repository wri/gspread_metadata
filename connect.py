import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


def get_metadata_wks():
    json_key = json.load(open('GlobalForestWatch-77b73e29bab8.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key('1QRHh01869cGnQLDDInVnNdx7b4OKIMfUKGhoXtyPU94').sheet1
    return wks


def get_metadata_keys():

    keys = {"name": 2,
            "title": 3,
            "summery": 4,
            "description": 5,
            "tags": 6,
            "place_keywords": 7,
            "geographic_extent": 8}

    return keys

def get_metadata_by_name(name):
    keys = get_metadata_keys()
    wks = get_metadata_wks()
    names = wks.col_values(keys["name"])
    if name in names:
        position = names.index(name)
    else:
        #add error handler here
        pass
    metadata = {}
    for key in keys:
        metadata[key] = wks.cell(position + 1, keys[key]).value

    return metadata

metadata = get_metadata_by_name("gfw_logging")

print metadata




