import sexpdata
from sexpdata import Symbol
import os


def write_sym_lib_table(filenames):
	s = [ Symbol('sym_lib_table'), [ Symbol('version'), 7 ] ]
	for fname in filenames:
		s.append([
			Symbol('lib'),
			[ Symbol('name'), fname ],
			[ Symbol('type'), 'KiCad' ],
			[ Symbol('uri'), os.path.join('${KIPRJMOD}/symbols', fname) ],
			[ Symbol('options'), '' ],
			[ Symbol('descr'), '' ],
		])
	with open('sym-lib-table', 'w') as f:
		sexpdata.dump(s, f)


def write_fp_lib_table(pretty_paths):
	s = [ Symbol('fp_lib_table'), [ Symbol('version'), 7 ] ]
	for path in pretty_paths:
		s.append([
			Symbol('lib'),
			[ Symbol('name'), path ],
			[ Symbol('type'), 'KiCad' ],
			[ Symbol('uri'), os.path.join('${KIPRJMOD}/footprints/', path) ],
			[ Symbol('options'), '' ],
			[ Symbol('descr'), '' ],
		])
	with open('fp-lib-table', 'w') as f:
		sexpdata.dump(s, f)




filenames = [ 'asdf.kicad_sym' ]
write_sym_lib_table(filenames)

filenames = [ 'asdf_foots.pretty' ]
write_fp_lib_table(filenames)

