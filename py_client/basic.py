import requests


# endpoint = 'https://httpbin.org/status/200'
endpoint = 'https://httpbin.org/anything'


get_response = requests.get(endpoint)  # HTTP Request

print(get_response.text)  # print raw text response
print(30 * '=')
print(get_response.json())  # print as a Python dict
