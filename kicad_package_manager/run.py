import glob
from importlib.machinery import SourceFileLoader
import os


commands = []
parser = None


def init_command(_parser):
	global parser
	parser = _parser
	subparsers = parser.add_subparsers(dest="command")

	init_files = glob.glob('kpm_modules/*/commands/__init__.py')
	for d in init_files:
		modulename = os.path.basename(os.path.dirname(d)).split("@")[0].replace("-","_")
		module = SourceFileLoader(modulename, d).load_module()

		if hasattr(module, 'register'):
			commands.append(module)
			module.register(subparsers)


def run_command(args):
	if args.command is None:
		parser.print_help()
		return

	for command_name, module in commands.items():
		if hasattr(module, 'run_command'):
			module.run_command(args)

