import requests
import json
import urllib
import logging

def getToken():
	consumer_key = "3MVG9g9rbsTkKnAUFgazceOHx1NTz._0YwU9ud8_DkwAfUDWtaixvlD97kN6E_auT7NR77K.ztrInAyL1dnCs"
	consumer_secret = "836889050885337481"
	username = "jon.byrum@gmail.com"
	password = "Hj3CodgmM6v9*8f"
	security_token = "6YKjSzTlNGB6h6In2cqRl5WO"

	payload = {
	    'grant_type': 'password',
	    'client_id': consumer_key,
	    'client_secret': consumer_secret,
	    'username': username,
	    'password': password + security_token
	}
	
	r = requests.post("https://login.salesforce.com/services/oauth2/token", 
		headers={"content-type":"application/x-www-form-urlencoded"},
		data=payload)
	token = "00D1I000001d2eU!AR8AQLbN2JNNuzi_Z_jKxjZrFdd4Trn.LBiiAEe5_u2ZM0DdDoci3G1Rw7nZcFl8oSfWjbSs6UUZrTBwd8Qqzz47cjsMmv0W"
	respDict = r.json()
	return respDict["access_token"]

def getData():
	token = getToken()
	url = "https://na73.salesforce.com/services/data/v20.0/query?q=SELECT+name+from+Contact"
	response = requests.get(url,
		headers={"Authorization": "Bearer " + token })

	if response.ok:
		respDict = response.json()
		names = []
		for contact in respDict["records"]:
			names.append(contact["Name"])
		return names
	else:
		response.raise_for_status
		print(response)

