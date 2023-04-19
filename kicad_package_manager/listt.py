from . import registry


def run_command(args):
	packages = registry.listt()
	print_packages(packages)


def print_packages(packages):
	print(f"All packages in registry:")
	print()
	for package in packages:
		release = package['releases'][-1]
		print(f"{package['name']}\tv{release['version']} - {release['author']}")
	print()
