from defines import getCreds, makeApiCall

def getInstagramAccount(params):

    endpointParams = {
        'access_token': params['access_token'],
        'fields': 'instagram_business_account'
    }
    
    
    url = params['endpoint_base'] + params['page_id']
    
    return makeApiCall(url, endpointParams, params['debug'])

# Get credentials and configure parameters
params = getCreds()
params['debug'] = 'no'
response = getInstagramAccount(params)

# Display account information
print("\n---- INSTAGRAM ACCOUNT INFO ----")
print("\nPage ID:")
print(response['json_data']['id'])
print("\nInstagram Business Account ID:")
print(response['json_data']['instagram_business_account']['id'])