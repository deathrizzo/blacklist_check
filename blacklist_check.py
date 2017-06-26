#!/usr/bin/env python3
'''
This script contains functions which access the MxToolBox API and get blacklist results for
IP addresses. to use against aws before attaching EIP's to instances 
'''

import json
import requests
import argparse
from configparser import ConfigParser
from pprint import pprint

## API Configuration Data
## Parses .mxtbx file for API Key
parser = ConfigParser()
parser.read('.mxtbx')
API_KEY = parser.get('mxtbx', 'key')
API_URL = 'https://api.mxtoolbox.com/api/v1'

parser = argparse.ArgumentParser()
parser.add_argument('-l','--list', nargs='+', type=str, help='IP Address or Addressees space sparated', required=True)
args = parser.parse_args()
ips = args.list

def get_blacklist_results(ip):
    '''
    Utilizes the MXToolBox API to do a Blacklist lookup on the supplied ip
    address.

    Args:
        ip (str): IP address to perform blacklist check on.

    Returns:
        json: Returns a json dictonary
    '''
    http_payload = {'Authorization': API_KEY }
    result = requests.get('{}/Lookup/blacklist/{}'.format(API_URL, ip), params=http_payload)
    result.raise_for_status()
    jresult = json.loads(result.text)
    return jresult

def main():
    for ip in ips:
      blacklist_results = get_blacklist_results(ip)
      if blacklist_results['Failed']:
        #pprint(blacklist_results['Failed'])
        print("{}\t Failed due to results".format(ip))
      else:
        print("{}\t IP is clean".format(ip))
        return 0

main()
