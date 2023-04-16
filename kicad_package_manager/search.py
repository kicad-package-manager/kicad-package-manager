from . import registry


def run_command(args):
	packages = registry.search(args.package_ref)
	print_packages(packages)


def print_packages(packages):
	print(f"Matching packages from registry:")
	print()
	for name, package in packages.items():
		release = package['releases'][-1]
		print(f"{name}\tv{release['version']} - {release['author']} - {release['artifact_url']}")
	print()
