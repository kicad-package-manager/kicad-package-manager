import json
from . import config
import requests
from .registry import get_release_for, repourl, get as get_package
import os
import io
import zipfile
from . import kicad_project_tables
import glob
import shutil
from .init import init_kpmjson


def init_command(parser):
	parser.add_argument('package_ref')
	parser.add_argument('--version', '-v', type=str, required=False)

def run_command(args):
	package_ref = args.package_ref

	if package_ref != '.':
		if not os.path.exists('kpm.json'):
			init_kpmjson()

		with open('kpm.json') as kpmf:
			kpmjson = json.loads(kpmf.read())

		name = args.package_ref
		package = get_package(name)
		if package is None:
			print(f"Could not find a package by name {name}")
			return

		if args.version is None:
			version = package['releases'][-1]['version']
		else:
			version = args.version
			version_found = False
			for release in package['releases']:
				if release['version'] == version:
					version_found = True
			if not version_found:
				print(f"Could not find version {version} for package {name}. Did you mean {package['releases'][-1]['version']}?")
				return

		if name in kpmjson['dependencies']:
			if kpmjson['dependencies'][name] == version:
				print(f"Package {name} is already installed! run `kpm install .` to load all of your libraries")
				return

		kpmjson['dependencies'][name] = version

		with open('kpm.json', 'w') as kpmf:
			kpmf.write(json.dumps(kpmjson, indent=4))

	install_from_config()


def install_from_config():
		with open('kpm.json') as kpmf:
			kpmjson = json.loads(kpmf.read())
		deps = {}
		if 'dependencies' in kpmjson:
			for depname, depversion in kpmjson['dependencies'].items():
				explore_deps(depname, depversion, deps)
			install_deps(deps)


def explore_deps(name, version, found_packages={}):
	if name in found_packages:
		if found_packages[name] != version:
			raise Exception(f"incompatible version for {name}: {version}, committed version is {found_packages[name]['version']}")
		else:
			return found_packages

	release = get_release_for(name, version)

	if release is None:
		print(f"ERROR: version {version} not found for package {name}\n\n")
		raise Exception("package version missing")

	found_packages[name] = release

	if 'dependencies' in release:
		for depname, depversion in release['dependencies'].items():
			explore_deps(depname, depversion, found_packages)

	return found_packages


def install_deps(deps):
	shutil.rmtree("./kpm_modules", ignore_errors=True)
	for package_name, release in deps.items():
		print(f"installing {package_name} @ {release['version']}")
		install_package(package_name, release['version'], release['artifact_url'])
	install_libraries()


def install_package(name, version, zip_url):
	package_dir = f"./kpm_modules/{name}@{version}/"
	os.makedirs(package_dir, exist_ok=True)
	if zip_url[0] == '/':
		urlzip_url = repourl + zip_url
	res = requests.get(zip_url)
	r = zipfile.ZipFile(io.BytesIO(res.content)).extractall(package_dir)


def install_libraries():
	# link symbol files
	symfiles = glob.glob("kpm_modules/**/symbols/*.kicad_sym", recursive=True)
	kicad_project_tables.write_sym_lib_table(symfiles)

	# link footprint files
	footfiles = glob.glob("kpm_modules/**/footprints/*.pretty", recursive=True)
	kicad_project_tables.write_fp_lib_table(footfiles)

	# install 3d models
	# install spice models
	# install plugins

