import argparse
from . import install
from . import init
from . import listt
from . import search
from . import show
from . import build
from . import upload

def main():
	parser = argparse.ArgumentParser(
		prog="kpm",
		description="KiCad Package Manager",
		epilog="manage kicad parts and plugins good"
	)

	subparsers = parser.add_subparsers(dest='command')
	
	commands = {
		"list":    listt,
		"search":  search,
		"show":    show,
		"init":    init,
		"install": install,
		"build":   build,
		"upload":  upload,
	}
	for command_name, module in commands.items():
		subparser = subparsers.add_parser(command_name)
		if hasattr(module, 'init_command'):
			module.init_command(subparser)

	args = parser.parse_args()

	for command_name, module in commands.items():
		if args.command == command_name:
			module.run_command(args)

