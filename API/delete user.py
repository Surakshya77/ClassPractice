import requests
import json


#base url:
base_url="https://reqres.in/api"

#auth key
auth_token="token ...token value"

def delete_request(user_id):
    url=base_url + f"/users/{user_id}"
    print("delete url:",url)
    headers={"Authorization":auth_token}
    response= requests.delete(url,headers=headers)
    assert response.status_code ==204
    print("Successful")

#call
delete_request(1)