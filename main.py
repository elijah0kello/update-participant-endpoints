import json
import requests
import logging 

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    with open('./endpoints.json','r') as f:
        endpoints = json.loads(f.read())

    url = "http://dev-centralledger-service/participants/payerfsp1/endpoints"
    
#    print(endpoints["endpoints"])

    for endpoint in endpoints["endpoints"]:
        payload = json.dumps(endpoint)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)    
        print(endpoint)
