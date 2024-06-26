""" 
- Sample client code that will perform the API call.
- During testing :
  a) Docker containers to be used.
  b) Ansible url module?
  c) Postman?
  d) How do i simulate web-browser testing?
"""

import requests


def get_country_details(name):
    # response = requests.get('http://localhost:5000/country', params={'name': name})

    response = requests.get(f"http://localhost:5000/country/{name}")

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()


if __name__ == "__main__":
    country_name = input("Enter the country name: ").capitalize()
    details = get_country_details(country_name)
    print(details)
