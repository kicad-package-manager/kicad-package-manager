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
		"list":    { "handler": listt,   "args": [], },
		"search":  { "handler": search,  "args": ["package_ref"], },
		"show":    { "handler": show,    "args": ["package_ref"], },
		"init":    { "handler": init,    "args": [], },
		"install": { "handler": install, "args": ["package_ref"], },
		"build":   { "handler": build,   "args": [], },
		"upload":  { "handler": upload,  "args": [], },
	}
	for command_name in commands:
		commands[command_name]['parser'] = subparsers.add_parser(command_name)
		for arg in commands[command_name]['args']:
			commands[command_name]['parser'].add_argument(arg)

	commands['build']['parser'].add_argument('--keep-build-dir', '-k', action="store_true", required=False, default=False)
	commands['install']['parser'].add_argument('--version', '-v', type=str, required=False)

	args = parser.parse_args()

	for command_name in commands:
		if args.command == command_name:
			commands[command_name]['handler'].run_command(args)

