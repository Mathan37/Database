from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import json
import requests
import pyrebase

config = {
	"apiKey": "AIzaSyBvgl8FOB_WTOB4GQbgDWHsSQyUo4YZLDc",
    "authDomain": "sample-c214b.firebaseapp.com",
    "databaseURL": "https://sample-c214b.firebaseio.com",
    "projectId": "sample-c214b",
    "storageBucket": "sample-c214b.appspot.com",
    "messagingSenderId": "486511878006",
    "appId": "1:486511878006:web:40604ab020c4d2137ea457",
    "measurementId": "G-FC6BYCYDDZ"

}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

class Manager(ScreenManager):
	pass

kv = Builder.load_file("database.kv")

class DataBaseApp(App):
	url = "https://sample-c214b.firebaseio.com/.json"
	def patch(self,JSON):
		to_database = json.loads(JSON)
		requests.patch(url=self.url,json = to_database)
	def put(self,JSON):
		to_database = json.loads(JSON)
		requests.put(url = self.url, json= to_database)
	def post (self,JSON):
		to_database = json.loads(JSON)
		requests.post(url = self.url , json= to_database)
	def delete (self,JSON):
		to_database = json.loads(JSON)
		requests.delete(url = self.url[:-5] + JSON + ".json")
	auth_key = "K39dFRIiGSSa7Jlbl5hLKmolZon7Dq0dEeK44U9E"
	def get(self):
		request=requests.get( self.url + "?auth=" + self.auth_key)
		print(request.json())
	def img_storage(self):
		self.y = self.root.ids.img.source 
		path_to_cloud = "Image/Rocket15.jpeg"
		storage.child(path_to_cloud).put(self.y)
	
	def build(self):
		return kv
if __name__ == "__main__":
	DataBaseApp().run()