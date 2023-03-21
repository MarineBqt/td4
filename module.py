import requests

def get_manor_ids(place_id):
    url=f"http://opendomesday.org/api/1.0/manor/{place_id}/"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    place_id = 1036  # First place id in Derbyshire
    manor_ids = get_manor_ids(place_id)
    print(manor_ids)
