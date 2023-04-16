import json
from . import config
import requests
from .registry import get_release_for
import os
import io
import zipfile
from . import kicad_project_tables
import glob
import shutil


def run_command(args):
	package_ref = args.package_ref

	if package_ref == '.':
		c = config.parse_config()
		deps = {}
		for depname, depversion in c.dependencies.items():
			explore_deps(depname, depversion, deps)
		install_deps(deps)


def explore_deps(name, version, found_packages={}):
	if name in found_packages:
		if found_packages[name] != version:
			raise Exception(f"incompatible version for {name}: {version}, committed version is {found_packages[name]['version']}")
		else:
			return found_packages

	release = get_release_for(name, version)
	found_packages[name] = release

	if 'dependencies' in release:
		for depname, depversion in release['dependencies'].items():
			explore_deps(depname, depversion, found_packages)

	return found_packages


def install_deps(deps):
	shutil.rmtree("./kpm_modules", ignore_errors=True)
	for package_name, release in deps.items():
		print(f"installing {package_name}")
		install_package(package_name, release['version'], release['artifact_url'])
	install_libraries()


def install_package(name, version, zip_url):
	package_dir = f"./kpm_modules/{name}@{version}/"
	os.makedirs(package_dir, exist_ok=True)
	res = requests.get(zip_url)
	r = zipfile.ZipFile(io.BytesIO(res.content)).extractall(package_dir)


def install_libraries():
	# link symbol files
	symfiles = glob.glob("**/*.kicad_sym", recursive=True)
	kicad_project_tables.write_sym_lib_table(symfiles)

	# link footprint files
	footfiles = glob.glob("**/*.kicad_mod", recursive=True)
	kicad_project_tables.write_fp_lib_table(footfiles)

	# install 3d models
	# install spice models
	# install plugins

