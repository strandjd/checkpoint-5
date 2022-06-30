import requests


def get_phone(variable1):
	phone = requests.get('http://localhost:5000/api?action=phone&name=Urban')
	return phone.text

def get_name(variable1):
	name = requests.get('http://localhost:5000/api?action=name&phone=0435-4355438')
	return name.text
