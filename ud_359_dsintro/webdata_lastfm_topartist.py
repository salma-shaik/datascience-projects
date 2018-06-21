import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    #
    # Once you've done this, return the name of the number 1 top artist in
    # Spain.

    artist_data = requests.get(url).text
    artist_data_dict = json.loads(artist_data)
    artist_data_dict_str = json.dumps(artist_data_dict, indent=2)
    top_artist = ''
    # print(artist_data_dict_str)

    for data in artist_data_dict['topartists']['artist']:
        # print('Inside for')
        if data['@attr']['rank'] == '1':
            print('Rank 1')
            top_artist = data['name']

    return top_artist  # return the top artist in Spain


api_get_request('# need api key to access the data')