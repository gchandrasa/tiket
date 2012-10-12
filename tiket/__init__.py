import urllib
import json
import requests

SERVER_API = 'https://api.master18.tiket.com'


def get_response(url, parameters):
    parameters['output'] = 'json'
    resource = '%s/%s?%s' % (SERVER_API, url, urllib.urlencode(parameters))
    response = requests.get(resource, verify=False)
    if response.ok:
        return json.loads(response.content)
    return None


def get_token(secretkey):
    parameters = {
        'method': 'getToken',
        'secretkey': secretkey
    }
    response = get_response('apiv1/payexpress', parameters)
    if response:
        return response['token']
    return None
