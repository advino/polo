import os
import requests
import string
import random
import datetime
from dotenv import load_dotenv
from fb import firebase

load_dotenv()
token = os.environ.get('access-code')

storage = firebase.storage()
database = firebase.database()

def random_string(stringLength=8):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

def upload_image(name):
	storage.child("images/" + name + ".jpg").put("photos/image.jpg")
	return storage.child("images/" + name + ".jpg").get_url(None)

def upload_to_rtdb(img_url):
	d = datetime.datetime.now()
	df = d.strftime("%c")
	dd = d.day
	dm = d.month
	dy = d.year
	dt = d.strftime("%X")
	data = {"name": "Polo Log", "full": df, "day": dd, "month": dm, "year": dy, "time": dt, "image": img_url} 
	database.child("logs").push(data)
	return df

def upload_to_arena(img_url, descrip):
	my_url = "https://api.are.na/v2/channels/polo-h8yksnejfas/blocks"
	headers = {'Authorization': 'BEARER ' + token}
	payload = {'title': 'Polo Log', 'description': descrip, 'source': img_url}
	polo = requests.post(my_url, data=payload, headers=headers)


name = random_string()
url = upload_image(name)
time_log = upload_to_rtdb(url)
upload_to_arena(url, time_log)
