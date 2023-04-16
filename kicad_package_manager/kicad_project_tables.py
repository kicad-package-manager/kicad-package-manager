import sexpdata
from sexpdata import Symbol
import os
import re


def write_sym_lib_table(files):
	print("writing sym")
	s = [ Symbol('sym_lib_table'), [ Symbol('version'), 7 ] ]
	for path in files:
		print(path)
		name = re.match(".*[\\/]([^\\/]+\.kicad_sym).*", path).group(1)[:-10]
		print(name)
		s.append([
			Symbol('lib'),
			[ Symbol('name'), name ],
			[ Symbol('type'), 'KiCad' ],
			[ Symbol('uri'), os.path.join('${KIPRJMOD}', path) ],
			[ Symbol('options'), '' ],
			[ Symbol('descr'), '' ],
		])
	with open('sym-lib-table', 'w') as f:
		sexpdata.dump(s, f)


def write_fp_lib_table(files):
	print("writing foot")
	s = [ Symbol('fp_lib_table'), [ Symbol('version'), 7 ] ]
	for path in files:
		print(path)
		name = re.match(".*[\\/]([^\\/]+\.pretty).*", path).group(1)[:-7]
		name.replace(".pretty", "")
		print(name)
		s.append([
			Symbol('lib'),
			[ Symbol('name'), name ],
			[ Symbol('type'), 'KiCad' ],
			[ Symbol('uri'), os.path.join('${KIPRJMOD}', path) ],
			[ Symbol('options'), '' ],
			[ Symbol('descr'), '' ],
		])
	with open('fp-lib-table', 'w') as f:
		sexpdata.dump(s, f)

