import requests

endpoint="http://localhost:8000/api/"


get_response=requests.post(endpoint,json={"title":"hello again","Price":50})
print(get_response.json())