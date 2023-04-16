import argparse
from . import install
from . import init
from . import listt
from . import search


def main():
	parser = argparse.ArgumentParser(
		prog="kpm",
		description="KiCad Package Manager",
		epilog="manage kicad parts and plugins good"
	)

	subparsers = parser.add_subparsers(dest='command')
	
	install_parser = subparsers.add_parser('install')
	install_parser.add_argument('package_ref')

	init_parser = subparsers.add_parser('init')

	list_parser = subparsers.add_parser('list')

	search_parser = subparsers.add_parser('search')
	search_parser.add_argument('package_ref')

	args = parser.parse_args()

	if args.command == 'install':
		install.run_command(args)

	if args.command == 'init':
		init.run_command(args)

	if args.command == 'list':
		listt.run_command(args)

	if args.command == 'search':
		search.run_command(args)

