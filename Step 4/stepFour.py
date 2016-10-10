import requests
import json
import re

myToken = {'token':'1affd2045f325a53eece718f96429a70'}
r = requests.post('http://challenge.code2040.org/api/prefix', params=myToken)
data = r.json()

print r.text
prefix = data["prefix"]
array = data["array"]

print prefix

def getStringArray():
    newArray =[]
    for strings in array:
        if not strings.startswith(prefix):
            oldString = json.dumps(strings)
            oldString = oldString.replace('\"', '')
            oldString = str(oldString)
            print oldString
            newArray.append(oldString)
    print newArray
    return newArray

jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'array': getStringArray()}

validate = requests.post ('http://challenge.code2040.org/api/prefix/validate',
    params=jsonReturn)
