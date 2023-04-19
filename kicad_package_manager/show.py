from . import registry


def init_command(parser):
	parser.add_argument('package_ref')


def run_command(args):
	package = registry.get(args.package_ref)
	if package is None:
		print(f"No package found in our registry for '{args.package_ref}'")
		return
	print_package(args.package_ref, package)


def print_package(name, package):
	print(f"Package: {name}")
	print(f"Owner: {package['owner']}")
	print(f"Homepage: {package['homepage']}")
	print()
	print("Releases:")
	for release in package['releases']:
		print(f"v{release['version']} - {release['author']} - {release['artifact_url']}")
		print("  dependencies:")
		if 'dependencies' in release:
			for dep, version in release['dependencies'].items():
				print(f"  - {dep}@{version}")
	print()
