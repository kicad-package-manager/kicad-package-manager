import json
from functools import lru_cache
import pathlib
import os

registry_json = """{
	"sample_kpm_package": {
		"owner": "danroblewis",
		"homepage": "https://github.com/danroblewis/sample_kpm_package",
		"releases": [
			{
				"version": "0.0.2",
				"artifact_url": "https://github.com/danroblewis/sample_kpm_package/archive/refs/tags/v0.0.2.zip",
				"author": "danroblewis"
			}
		]
	},
	"sample_kpm_package_2": {
		"owner": "danroblewis",
		"homepage": "https://github.com/danroblewis/sample_kpm_package_2",
		"releases": [
			{
				"version": "0.0.2",
				"artifact_url": "https://github.com/danroblewis/sample_kpm_package_2/archive/refs/tags/v0.0.2.zip",
				"author": "danroblewis",
				"dependencies": {
					"sample_kpm_package": "0.0.2"
				}
			}
		]
	},
	"sample_kpm_package_3": {
		"owner": "danroblewis",
		"homepage": "https://github.com/danroblewis/sample_kpm_package_3",
		"releases": [
			{
				"version": "0.0.2",
				"artifact_url": "https://github.com/danroblewis/sample_kpm_package_3/archive/refs/tags/v0.0.2.zip",
				"author": "danroblewis",
				"dependencies": {
					"sample_kpm_package_2": "0.0.2"
				}
			}
		]
	}
}"""

temporary_registry = json.loads(registry_json)

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

