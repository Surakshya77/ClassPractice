import requests
import json

# base url:
base_url = "https://reqres.in/api"

# auth key
auth_token = "token ...token value"

def get_user_by_id(user_id):
    url = f"{base_url}/users/{user_id}"
    print("Get user by ID: " + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=6)
    print("JSON Get response body:", json_str)
    print("...........Get user by ID is done ........")
    print("...........==============............")

# call
get_user_by_id(5)
