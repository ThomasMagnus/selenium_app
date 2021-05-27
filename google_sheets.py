import requests
from typing import final


class GoogleSheets:

    def __init__(self):
        self.LINK_FORM: final(str) = 'https://api.sheety.co/c7c8422e4e346e779a525b52a6d7be14/entryJob/job'

    def get_address(self):
        res = requests.get(self.LINK_FORM).json()
        address = res['job'][0]['what\'sTheAddressOfTheProperty?']
        return address
