import requests

API_URL = "https://jsonplaceholder.typicode.com/"


def list(users):
    response = requests.get(API_URL + "/users/")

    if response.status_code == 200:
        return response.json()
    
    return False


def create(users):
    response = requests.post(API_URL + "/users/", json=users)

    if response.status_code == 201:
        return response.json()

    return False


def read(users):
    response = requests.get(API_URL + "/users/" + str(users))

    if response.status_code == 200:
        return response.json()
    
    return False


def update(users):
    response = requests.put(API_URL + "/users/" + str(users["id"]), json=users)

    if response.status_code == 200:
        return response.json()

    return False


def delete(users):
    response = requests.delete(API_URL + "/users/" + str(users["id"]))

    if response.status_code == 204:
        return response.json()

    return False
