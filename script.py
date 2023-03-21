import requests

# Set up the URL 
url='http://opendomesday.org/api/1.0/county/dby'

# Send the API request and get the response
place_ids = requests.get(url)

# Print the list of place IDs
print(place_ids.json())
