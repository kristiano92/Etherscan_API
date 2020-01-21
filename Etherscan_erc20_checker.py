import json
import requests
import sys

def erc20_checker(address, api_key):
    """Function uses etherscan API to check that given address is an erc20 contract."""

    url = "https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=" + address + "&apikey=" + api_key
    response = requests.get(url)

    if response.status_code != 200:
        print(response.text)

    address_content = response.json()
    result = address_content.get("result")
    result_int = int(result)

    if result_int > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    _address, _api_key = sys.argv[1:3]
    print(erc20_checker(_address, _api_key))
