import requests
import json

INSTAGRAM = {
	"access_token":"272246557.baf3914.069a0fb4d48e45b586e2884032d24dfd",
}



def get_instagram_pics():
	url = 'https://api.instagram.com/v1/users/3532778/media/recent/?access_token='
	r = requests.get(url+INSTAGRAM['access_token'])
	if(r.ok):
		images = r.json()['data']
		links = []
		for image in images:
			links.append(image['images']['standard_resolution']['url'])
		return links