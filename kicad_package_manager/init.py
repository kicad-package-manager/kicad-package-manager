import re
import glob
import json
import os
from . import registry
from . import config


def run_command(args):
    init_kpmjson()


def init_kpmjson(search_existing=True):
    modules = set()

    if search_existing:
        # get footprints from schematics
        for fname in glob.glob('**.kicad_sch'):
            with open(fname) as f:
                text = f.read()
                footprints = re.findall(r'\(\s*property\s+"Footprint"\s+"[^"]+"', text)
                footprints = [ re.sub('^.* "Footprint" "', '', fp).replace('"','') for fp in footprints]
                for ft in footprints:
                    modules.add("kicad_lib_footprints_" + re.sub(':.*', '', ft))

            symbols = re.findall(r'\(\s*symbol\s+"[^"]+:', text)
            symbols = [ re.sub('^.*"', '', s).replace(':','') for s in symbols]
            for s in symbols:
                modules.add("kicad_lib_symbols_" + s)

        # get footprints from pcb files
        for fname in glob.glob('**.kicad_pcb'):
            with open(fname) as f:
                text = f.read()
                footprints = re.findall(r'\(\s*footprint\s+"[^"]+"', text)
                footprints = [ re.sub('.*"', '', re.sub(':.*', '', fp)) for fp in footprints]
                for ft in footprints:
                    modules.add("kicad_lib_footprints_" + ft)

    deps = {}
    for modulename in sorted(modules):
        package = registry.get(modulename)
        if package:
            deps[modulename] = package['releases'][-1]['version']

    project_name = os.path.basename(os.getcwd())

    c = config.Config({
        "name": project_name,
        "dependencies": deps
    })

    # create our kpm.json config file
    with open('kpm.json', 'w') as f:
        f.write(c.toJSON())

    # add to or create .gitignore
    if os.path.exists('.gitignore'):
        with open('.gitignore') as fr:
            if 'kpm_modules' not in fr.read():
                with open('.gitignore', 'a') as fw:
                    fw.write("\nkpm_modules")
                    fw.write("\n.kpmrc")
                    fw.write("\npackage.zip")
                    fw.write("\nbuild")
    else:
        with open('.gitignore', 'w') as f:
            f.write("kpm_modules\n")



