"""
- Sample client code that will perform the API call.
- During testing :
  a) Docker containers to be used.
  b) Ansible url module?
  c) Postman?
  d) How do i simulate web-browser testing?
"""

import requests
from time import sleep

def get_country_details(name):
    """
    - Function to do get()
    - Can be either all or specific name.
    """
    # response = requests.get('http://localhost:5000/country', params={'name': name})

    response = requests.get(f"http://localhost:5000/country/{name}")

    # return response  # Should be json format already?

    if response.status_code == 200:
        return response.json()
    else:
        return "Error! Server could be unreachable or the database is faulty"
    
def test_function():
    """
    - Function to test queries
    - To be used on containers
    """
    countries = ["Kenya", "UGAnda", "Angola", "Australia", "Burundi", "USA", "Tanzania"]
    
    for i in range(50):
        for name in countries:
            print(get_country_details(name))
            sleep(1)


if __name__ == "__main__":
    # country_name = input("Enter the country name[or all]: ").capitalize()
    # details = get_country_details(country_name)
    # print(details)
    test_function()
