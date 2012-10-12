from tiket import get_response


def search(token, keyword, startdate, night, adult=1):
    parameters = {
        'q': keyword,
        'startdate': startdate,
        'night': night,
        'adult': adult,
        'token': token
    }
    return get_response('search/hotel', parameters)
