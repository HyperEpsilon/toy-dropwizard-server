import json
import requests

def test_code():
    r = requests.get()
    json_response = r.json()
    assert(json_response["code"] == 404)

def test_message():
    r = requests.get()
    json_response = r.json()
    assert(json_response["message"] == "")

