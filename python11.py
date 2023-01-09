import requests
import json
url = "http://10.71.71.1:5034/process"
data1 = {'remote_daddr': '103.21.124.123'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data1), headers=headers)
print(r.json())
#
