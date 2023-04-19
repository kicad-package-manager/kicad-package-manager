import argparse
from . import install
from . import init
from . import listt
from . import search
from . import show
from . import build
from . import upload
from . import run
from . import init_package


def main():
	parser = argparse.ArgumentParser(
		prog="kpm",
		description="KiCad Package Manager",
		epilog="manage kicad parts and plugins good"
	)

	subparsers = parser.add_subparsers(dest='_command')
	
	commands = {
		"list":    listt,
		"search":  search,
		"show":    show,
		"init":    init,
		"install": install,
		"build":   build,
		"upload":  upload,
		"run":     run,
		"init_package": init_package,
	}
	for command_name, module in commands.items():
		subparser = subparsers.add_parser(command_name)
		if hasattr(module, 'init_command'):
			module.init_command(subparser)

	args = parser.parse_args()

	if args._command is None:
		parser.print_help()
		return

	for command_name, module in commands.items():
		if args._command == command_name:
			module.run_command(args)

