import requests

json_data = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

json_to_dict = json_data.json()

print(json_to_dict[0])

pull_counter = {}

for pull in json_to_dict:
    creator = pull["user"]["login"]
    if creator in pull_counter:
        pull_counter[creator] += 1
    else:
        pull_counter[creator] = 1 

print(pull_counter)

'''
for i in range(len(json_to_dict)):
    print(json_to_dict[i]["user"]["login"])

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls") 
print(response)
'''

