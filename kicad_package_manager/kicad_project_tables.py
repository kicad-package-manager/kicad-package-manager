import sexpdata
from sexpdata import Symbol
import os


def write_sym_lib_table(files):
	print("writing sym")
	s = [ Symbol('sym_lib_table'), [ Symbol('version'), 7 ] ]
	for path in files:
		s.append([
			Symbol('lib'),
			[ Symbol('name'), path.replace('kpm_modules/','') ],
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
		s.append([
			Symbol('lib'),
			[ Symbol('name'), path.replace('kpm_modules/','') ],
			[ Symbol('type'), 'KiCad' ],
			[ Symbol('uri'), os.path.join('${KIPRJMOD}', path) ],
			[ Symbol('options'), '' ],
			[ Symbol('descr'), '' ],
		])
	with open('fp-lib-table', 'w') as f:
		sexpdata.dump(s, f)

