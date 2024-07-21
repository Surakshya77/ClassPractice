import requests
import json


#base url:
base_url="https://reqres.in/api"

#auth key
auth_token="token ...token value"

def get_request(page):
    url=base_url +"/users"
    print("Get user:" +url)
    headers={"Authorization": auth_token}
    response=requests.get(url,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data, indent=6)
    print("Json Get response body:",json_str)
    print("...........Get user is done ........")
    print("...........==============............")

#call
get_request(1)
