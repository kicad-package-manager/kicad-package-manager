import json
import os
from . import init

def init_command(parser):
	parser.add_argument('project_name')


def run_command(args):
	# make directory for project
	# make directory in that for each of the things
	# make a .gitkeep file in each directory
	# init with the kpm init function
	name = args.project_name
	os.makedirs(name)
	os.chdir(name)
	dirs = [
		'commands',
		'symbols',
		'footprints',
		'3dmodels',
		'plugins',
		'simulation',
		'subsheets',
		'tests',
		'scripts',
	]
	for d in dirs:
		os.makedirs(d)
		with open(os.path.join(d, ".gitkeep"), 'w') as f:
			f.write("keep")

	init.init_kpmjson()

	# also make example git workflows

	os.chdir('..')
