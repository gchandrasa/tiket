from tiket import get_response


def search(token, origin, destination, date):
    parameters = {
        'd': origin,
        'a': destination,
        'date': date,
        'token': token
    }
    return get_response('search/train', parameters)
