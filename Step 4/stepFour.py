# Author: © Juan Zamudio 2016
# Date: October 8, 2016
# Code2040-Tech-Assessment: Step Four
#
# Makes a POST request with personal API token to receive prefix string
# and string array. Then checks to see if strings in string array start
# with prefix. If so, places them in a new string array which is sent
# via POST request along with token to validation url as a JSON dictionary.

import requests
import json

# API token
myToken = {'token':'1affd2045f325a53eece718f96429a70'}

# POST request to get prefix and string array
r = requests.post('http://challenge.code2040.org/api/prefix', data=myToken)

# Save request reponse as JSON dictionary
data = r.json()

print r.text # Print request response
prefix = data["prefix"] # Get prefix string
stringArray = data["array"] # Get array of strings

print prefix # Print prefix string

newArray = [] # Initalize empty array for strings not with prefix

# Checks if strings in the array of strings do not start with the prefix
# string. If the string does not start with the prefix, then append string
# to the newArray.
for strings in stringArray:
    if not strings.startswith(prefix):
        newArray.append(strings)

print newArray # Print newArray contents

# JSON dictionary with token and newArray
jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'array': newArray}

# POST request to validate if array contains strings without prefix
validate = requests.post('http://challenge.code2040.org/api/prefix/validate',
    json=jsonReturn)

# Print validation request response
print validate.text
