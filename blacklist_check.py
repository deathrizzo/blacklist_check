#!/usr/bin/env python3
'''
This script contains functions which access the MxToolBox API and get blacklist results for
IP addresses. to use against aws before attaching EIP's to instances 
'''

import json
import requests
from pprint import pprint


## API Configuration Data
##TODO: Remove this API key from the file and utilize alterante methods for supplying
##      the API key.
API_KEY = 'APIKEYHERE'
API_URL = 'https://api.mxtoolbox.com/api/v1'

def get_blacklist_results(ip):
    '''
    Utilizes the MXToolBox API to do a Blacklist lookup on the supplied ip
    address.

    Args:
        ip (str): IP address to perform blacklist check on.

    Returns:
        json: Returns a json dictonary
    '''
    http_payload = {'Authorization': API_KEY}
    result = requests.get('{}/Lookup/blacklist/{}'.format(API_URL, ip), params=http_payload)
    result.raise_for_status()
    jresult = json.loads(result.text)
    return jresult

def main():
    blacklist_results = get_blacklist_results('IP HERE')
    if blacklist_results['Failed']:
        pprint(blacklist_results['Failed'])
				print("This IP is blacklisted")
    else:
        return 0

main()
