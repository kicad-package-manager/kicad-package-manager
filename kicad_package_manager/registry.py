from functools import lru_cache
import pathlib
import os
import requests

temporary_registry = requests.get("https://raw.githubusercontent.com/danroblewis/kicad-package-index/main/registry.json").json()


@lru_cache
def get_release_for(package_name, version):
	package = get(package_name)
	if package is None:
		raise Exception(f"no package exists by name {package_name}")

	for release in package['releases']:
		if release['version'] == version:
			return release

	return None


def get_zip_url_for(package_name, version):
	release = get_release_for(package_name, version)
	return release['artifact_url']


def search(package_name):
	matches = []
	for package in temporary_registry:
		if package_name in package['name']:
			matches.append(package)
	return matches


def get(package_name):
	for package in temporary_registry:
		if package['name'] == package_name:
			return package
	return None


def listt():
	return temporary_registry
