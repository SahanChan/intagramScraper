from defines import getCreds, makeApiCall

def getUserPages(params):
    endpointParams = {'access_token': params['access_token']} 
    url = params['endpoint_base'] + 'me/accounts'  
    
    return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = 'no'
response = getUserPages(params)

print("\n---- FACEBOOK PAGE INFO ----")
print("\nPage Name:")
print(response['json_data']['data'][0]['name'])
print("\nPage Category:")
print(response['json_data']['data'][0]['category'])
print("\nPage ID:")
print(response['json_data']['data'][0]['id'])