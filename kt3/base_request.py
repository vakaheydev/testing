import pprint

import requests


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        # set headers, authorisation etc

    def _request(self, url, request_type, data=None):
        if request_type == 'GET':
            response = requests.get(url)
        elif request_type == 'POST':
            response = requests.post(url, json=data)
        else:
            response = requests.delete(url)

        # log part
        pprint.pprint(f'{request_type} example')
        # pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        # pprint.pprint(response.reason)
        # pprint.pprint(response.text)
        # pprint.pprint(response.json())
        # pprint.pprint('**********')
        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET')
        return response.json()

    def post(self, endpoint, endpoint_id, body):
        # post('shop')
        # shop
        if endpoint_id == '':
            url = f'{self.base_url}/{endpoint}'
        else:
            url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body)
        return response.json()

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()
