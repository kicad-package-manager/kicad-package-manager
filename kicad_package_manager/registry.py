from functools import lru_cache
import pathlib
import os
import requests


repourl = "http://vps-407d02be.vps.ovh.us:80"


def get_release_for(package_name, version):
	package = get(package_name)
	if package is None:
		raise Exception(f"no package exists by name {package_name}")

	if version == 'latest':
		return package['releases'][-1]

	for release in package['releases']:
		if release['version'] == version:
			return release

	return None


def get_zip_url_for(package_name, version):
	release = get_release_for(package_name, version)
	url = release['artifact_url']
	if url[0] == '/':
		url = repourl + url
	return url


def search(package_name):
	r = requests.get(f"{repourl}/packages?term={package_name}")
	if r.status_code != 200:
		print("couldnt get packages list from registry")
		print(r)
		print(r.status_code)
		print(r.content)
		raise Exception("nooo")
	return r.json()


def get(package_name):
	r = requests.get(f"{repourl}/package/{package_name}")
	if r.status_code != 200:
		print("couldnt get package from registry")
		print(r)
		print(r.status_code)
		print(r.content)
		raise Exception("nooo")
	return r.json()


def listt():
	return search("")
