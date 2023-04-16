from . import registry


def run_command(args):
	package = registry.search(args.package_ref)
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
		for dep, version in release['dependencies'].items():
			print(f"  - {dep}@{version}")
	print()
