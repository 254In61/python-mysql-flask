import requests

def get_country_details(name):
    response = requests.get('http://localhost:5000/country', params={'name': name})
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

if __name__ == "__main__":
    country_name = input("Enter the country name: ")
    details = get_country_details(country_name)
    print(details)
