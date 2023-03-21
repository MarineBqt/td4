import requests
import pandas as pd
#Get the IDs of all places in a given county
def get_place_ids(county):
    url=f'http://opendomesday.org/api/1.0/county/{county}'
    response = requests.get(url)
    place_ids = response.json()
    return place_ids


def get_manor_ids(place_id):
    url=f"http://opendomesday.org/api/1.0/manor/{place_id}/"
    response = requests.get(url)
    data = response.json()
    return data['place']

def get_manor_info(place_id):
    url=f"http://opendomesday.org/api/1.0/manor/{place_id}/"
    response = requests.get(url)
    data = response.json()
    geld = data['geld']
    total_ploughs = data['totalploughs']
    return (geld, total_ploughs)

if __name__ == '__main__':
    county = 'dby'
    #place_ids = get_place_ids(county)
    place_ids=[1036,2558]
    #place_ids = [place['id'] for place in place_ids['places_in_county']]
    manor_ids = []
    manor_info=[]
    for id in place_ids:
        manor_ids.append(get_manor_ids(id))
        manor_info.append(get_manor_info(id))

    #Create a Pandas DataFrame with the information
    df = pd.DataFrame(manor_info, columns=['geld', 'total_ploughs'])
    print(df.head())

    #Compute the sum of geld paid and total ploughs owned in Derbyshire
    total_geld = df['geld'].sum()
    total_ploughs = df['total_ploughs'].sum()

    print('Total geld paid in Derbyshire:', total_geld)
    print('Total ploughs owned in Derbyshire:', total_ploughs)
    
    #print(manor_ids)
    #print(place_ids)
