
import requests
import json

def getCreds():
    creds = dict()
    creds['access_token'] = 'EAA3J9HD9158BO5jtIynZBtHTeoSZAZAZBAgIgQyOggEUn50RClHoZAZCd0vdENPJk51emZBh9JbQx8y81AStdvQFaqTToyug6igPREKBslzf5XD3LKRgc7jNGMukgceIHW9K1z5jCgDb2M0jgVNix59P1RF5zy9uW1K43FIaZC6aNv0Wb8WIQdLsvYEZB'
    creds['client_id'] = '3881226402125727'
    creds['client_secret'] = 'f94ba2d3ab049f7512736303173ecac5'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v22.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] +'/'
    creds['debug'] = 'no'

    return creds


def makeApiCall( url,endpointParams,debug='no'):
    data = requests.get(url,endpointParams)

    response = dict()
    response['url']=url
    response['endpoint_params']= endpointParams
    response['endpoint_params_pretty'] =json.dumps(endpointParams,indent=4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'],indent=4)

    if('yes' == debug):
        displayApiCallData(response)
    
    return response


def displayApiCallData(response):
    print("\nUrl: ")
    print(response['url'])
    print("\nEndpoint Params: ")
    print(response['endpoint_params_pretty'])
    print("\nResponse: ")
    print(response['json_data_pretty'])
