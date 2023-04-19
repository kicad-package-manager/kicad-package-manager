from . import registry


def init_command(parser):
	parser.add_argument('package_ref')


def run_command(args):
	packages = registry.search(args.package_ref)
	print_packages(packages)


def print_packages(packages):
	print(f"Matching packages from registry:")
	print()
	for package in packages:
		release = package['releases'][-1]
		print(f"{package['name']}\tv{release['version']} - {release['author']}")
	print()
