import requests


def handle_requests(method, url, params=None):
    if params is not None:
        if method == "GET":
            request = requests.get(url, params=params)
            return request.json()

        elif method == "POST":
            requests.post(url, data=params)
            return {'message': 'success!'}
    else:
        request = requests.get(url)
        return request.json()




