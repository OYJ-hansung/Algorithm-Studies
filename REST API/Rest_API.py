import requests
import json

url = 'https://jsonmock.hackerrank.com/api/food_outlets?city={}'.format('Houston')
# response = requests.request("GET", url, headers={}, data={}) #POST man을 활용
response = requests.get(url)
code = response.status_code
data = response.content # type = byte
data_json = json.loads(data) #type = dictionary
print(data_json['data'])

# print('Json Data :', data_json)

