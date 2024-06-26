"""
- Test GET method
"""

import requests

def get_country_details(name):
    """
    - Function that does the get() to obtain the results.
    - Ideally should be imported from modules!
    """
    # response = requests.get('http://localhost:5000/country', params={'name': name})

    response = requests.get(f'http://localhost:5000/country/{name}')
    return response

    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     return response.json()
def test_get_kenya():
    """
    Function to test get method
    """
    # Do I need the ID?
    assert get_country_details("Kenya") == {
                                            'capital': 'Nairobi',
                                            'country': 'Kenya',
                                            'id': 1,
                                            'leader': 'William Ruto',
                                            'population': 55678333
                                            }

def test_get_rwanda():
    """
    Function to test get method
    """
    # Do I need the ID?
    assert get_country_details("Rwanda") == {
                                             'capital': 'Kigali',
                                             'country': 'Rwanda',
                                             'id': 4,
                                             'leader': 'Paul Kagame',
                                             'population': 19678975
                                             }

def test_get_nocountry():
    """
    Function to test get method
    """
    assert get_country_details("nocountry") == {'error': 'Country not found'}
