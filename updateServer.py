# Almost entire format taken from PythonAnywhere's API example: https://help.pythonanywhere.com/pages/API/

import requests
username = "ryanmeoni"
api_token = "b7a7ccbbda23851d8abcffeba08ba3d4a27b8e8d"
domain_name = "ryanmeoni.pythonanywhere.com"

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
        username=username, domain_name=domain_name
    ),
    headers={'Authorization': 'Token {token}'.format(token=api_token)}
)
if response.status_code == 200:
    print('reloaded OK')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
