import requests
import json
import random
import string
#base url:
base_url="https://reqres.in/api"

#auth key
auth_token="token ...token value"


def generate_random_email():
    domain = "automation.com"
    email_length = 8
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#post request
def put_request(user_id):
    url=base_url + f"/users/{user_id}"
    print("put url as:",url)
    headers={"Authorization":auth_token}
    data={
        "name": "Surakshya",
        "email":generate_random_email(),
        "phone_number":"9876544",
        "job": "QA Learner"
    }

    response = requests.put(url,json=data,headers=headers)
    json_data=response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json post response data:",json_str)
    assert response.status_code ==200
    print("Successful")

#call
put_request(774)