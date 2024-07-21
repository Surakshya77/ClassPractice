import requests
import json

## base url:
base_url = "https://reqres.in/api"

# auth key
auth_token = "token ...token value"


#post request
def post_request(user_names):
    url = base_url + "/users/"
    print("Post url : ",url)
    headers = {"Authorization": auth_token}
    user_ids = []

    for name in user_names:
        data = {
            "name": name,
            "job": "QA Learner"
        }
        response = requests.post(url, json=data, headers=headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=6)
        print("Json data post response:", name, ":", json_str)
        user_id = json_data.get("id")
        if user_id:
            user_ids.append(user_id)
        assert response.status_code ==201
        assert "name" in json_data
        print(".........Post/user is created successfully", name, ".............")

    return user_ids


#user name example:
user_names = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU"]
user_ids = post_request(user_names)
print("Created user Id:", user_ids)
