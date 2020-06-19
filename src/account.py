import json

def getAccounts():
    f = open("./../account/account.json")
    j = json.load(f)
    return j

def getMaster():
    f = open("./../account/account.json")
    j = json.load(f)
    for user in j:
        if user['type'] == "master":
            return user
    return None