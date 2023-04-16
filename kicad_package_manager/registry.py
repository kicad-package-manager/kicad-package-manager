from functools import lru_cache
import pathlib
import os
import requests

temporary_registry = requests.get("https://raw.githubusercontent.com/danroblewis/kicad-package-index/main/registry.json").json()


@lru_cache
def get_release_for(package_name, version):
	if package_name not in temporary_registry:
		raise Exception(f"no package exists by name {package_name}")

	releases = temporary_registry[package_name]['releases']
	found = None
	for release in releases:
		if release['version'] == version:
			return release


def get_zip_url_for(package_name, version):
	release = get_release_for(package_name, version)
	return release['artifact_url']


def search(package_name):
	package = temporary_registry[package_name]
	return package


def listt():
	return temporary_registry
