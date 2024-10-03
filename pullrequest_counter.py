import requests

url = ('https://api.github.com/repos/kubernetes/kubernetes/pulls')

json_response = requests.get(url)

if json_response.status_codes == 200:
    pull_request = json_response.json()

    pull_counter = {}

    for pull in pull_request:
        creator = pull["user"]["login"]
        if creator in pull_counter:
            pull_counter[creator] += 1
        else:
            pull_counter[creator] = 1

    print("PR creators and counts:")

    for creator,count in pull_counter.items():
        print(f"{creator}: {count} PRs")

else:
    print(f"Failed to fetch data. Status code: {requests.status_codes}")




