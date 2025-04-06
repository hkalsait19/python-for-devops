import requests

responce = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
responce_mine = requests.get("https://github.com/hkalsait19/python-for-devops")

print(responce)
print(responce.status_code)

print(responce_mine)
print(responce_mine.status_code)

complete_details = responce.json()
# print(complete_details[0]["id"])
# print(complete_details[0]["html_url"])
# print(complete_details[0]["title"])
# print(complete_details[0]["state"])
# print(complete_details[0]["user"]["login"])

for user_name in range(len(complete_details)):
    print(complete_details[user_name]["user"]["login"])