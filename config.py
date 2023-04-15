import json


class Config:
	defaults = {
		"name": "",
		"version": "0.0.0",
		"author": "",
		"homepage": "",
		"commands": {},
		"dependencies": {},
	}

	def __init__(self, j={}):
		self.j = j
	
	def __getattr__(self, name):
		if name in self.j:
			return self.j[name]
		elif name in self.defaults:
			return self.defaults[name]
		else:
			raise Exception(f"unknown config value '{name}'")

	def to_json(self):
		d = {}
		for k in self.defaults:
			d[k] = self.__getattr__(k)
		return json.dumps(d)


def parse_config(filepath="./kpm.json"):
	with open(filepath) as f:
		return Config(json.load(f))


