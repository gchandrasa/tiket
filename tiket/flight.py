from tiket import get_response


def search(token, origin, destination, date, **kwargs):
    parameters = {
        'd': origin,
        'a': destination,
        'date': date,
        'token': token
    }
    return get_response('search/flight', parameters)


def nearest_airport(token, latitude, longitude):
    parameters = {
        'latitude': latitude,
        'longitude': longitude,
        'token': token
    }
    return get_response('flight_api/getNearestAirport', parameters)


