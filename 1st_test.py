import requests
URL = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=54f9ce65a45ea7a1e6bfb84eeee26c83&user_id=199228782%40N02&format=json&nojsoncallback=1"
response = requests.get(URL)
print(response.status_code)  
print(response.json())