import requests
from datetime import datetime

TOKEN = "ozimedeumole@gmail.com"
USERNAME = "umole"
GRAPH_ID = "codinggraph1"

pixella_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixella_endpoint, json=user_params)
# print(response.text)
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

graph_configuration = {
    "id": GRAPH_ID,
    "name": "codinghabit",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}
graph_body = {
    "date": formatted_date,
    "quantity": int(input("How many commits did you make today? ")),
}
graph_header = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_body, headers=graph_header)
print(response.text)



