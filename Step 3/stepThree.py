# Author: © Juan Zamudio 2016
# Date: October 8, 2016
# Code2040-Tech-Assessment: Step Three
#
# Makes a POST request with personal API token to receive a string and
# an array of strings (i.e. needle and a haystack respectively). Reponse
# is saved as a JSON dictionary. Then checks to see if needle
# is in the haystack. Index value is updated accordingly in loop. Token
# and index value are put into JSON dictionary and POST request
# is made to validation url

import requests
import json

# The API token
myToken = {'token':'1affd2045f325a53eece718f96429a70'}

# The POST request to receive the string and the array of strings
r = requests.post('http://challenge.code2040.org/api/haystack', params=myToken)

# Save request reponse as JSON dictionary
data = r.json()

print r.text # Print request response

needle = data["needle"] # Get needle from the dictionary
haystack = data["haystack"] # Get haystack from the dictionary

# Checks to see if the strings in the haystack are equal to the needle.
# If so, it will immediately break from the loop and index will be the
# index at which the needle was found in the haystack.
# Otherwise, index value increases and the next word in the haystack
# is checked to see if it is equal to the needle.
index = 0
for hay in haystack:
    if hay == needle:
        print index
        print haystack[index]
        break
    else:
        index += 1

# JSON dictionary of the token and the index
jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'needle': index}

# POST request to check for index validation
validate = requests.post ('http://challenge.code2040.org/api/haystack/validate',
    params=jsonReturn)

# Print validation request response
print validate.text
