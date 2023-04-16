import json
from functools import lru_cache
import pathlib
import os

temporary_registry = json.load(open(os.path.join(pathlib.Path(__file__).parent, 'registry.json')))


def search(package_name):
	pass


@lru_cache
def get_release_for(package_name, version):
	if package_name not in temporary_registry:
		raise Exception(f"no package exists by name {package_name}")

	releases = temporary_registry[package_name]['releases']
	found = None
	for release in releases:
		print(release)
		if release['version'] == version:
			return release


def get_zip_url_for(package_name, version):
	release = get_release_for(package_name, version)
	return release['artifact_url']

