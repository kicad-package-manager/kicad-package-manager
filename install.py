import json
import config


def run_command(args):
	package_ref = args.package_ref

	if package_ref == '.':
		config = config.parse_config()
		# this is to write the config file
		
		# delete current kicad_modules directory
		# get configs for each dependency-at-version
		# attempt to resolve dependency graph
		# install libraries



