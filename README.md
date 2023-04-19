# KiCad Package Manager


This is a package manager for KiCad symbols, footprints, 3d models, simulation files, and hierarchical sheets.



Goal
----

Create a format for distributing the following kind of KiCad features:

* Symbols
* Footprints
* 3D Models
* SPICE Simulation Code
* Sub-sheets
* Unit Tests
* Command Runner
* Plugins

Projects can be created that programmatically generate these files.

Currently Supports:

* Symbols
* Footprints

Up Next:

* Subsheets
* Command Runner
* 3D Models



Installing KPM
--------------

Open the "KiCad Command Prompt"

```bash
pip3 install kicad-package-manager
```

In your KiCad project directory, run

```bash
kpm init
```

Then edit your `kpm.json` file as needed.


How to Install a Package
------------------------

Find a package you want to use:

```bash
kpm list
kpm list | grep something
kpm search something
kpm show some_package
```

Then edit the `dependencies` list in your `kpm.json` to include a package and version. Example:

```json
{
	"name": "cool-project",
	"version": "0.0.1",
	"author": "danroblewis",
	"homepage": "http://githab.info/magic/stuff",
	"commands": {
		"test": "./fictional-spice-tester"
	},
	"dependencies": {
		"kpm-jlcpcb-basic": "0.0.5",
		"eurorack-parts": "0.0.1"
	}
}
```

How to Create a Package
-----------------------

Create a directory, it can be a KiCad project directory or any directory. Probably put it under version control with something like git.

```bash
kpm init
```

This creates a `kpm.json` file. Add the dependencies your package will require to the `dependencies` list.

Your package will include your `kpm.json` file and any of these directories if they are present:

```
/symbols
/footprints
/commands
/3dmodels
/plugins
/simulation
/subsheets
/tests
/commands
```

To build the package

```bash
kpm build
```

You should now have a `package.zip` file in your project directory.

To upload a package to the registry, first create a `~/.kpmrc` file:
```json
{
	"name": "yourname",
	"token": "arbitrarytokenonlyyouknow"
}
```

Then update the version in your `kpm.json` file.

Then run
```bash
kpm upload
```

You should then see your package in the `kpm search <yourpackagename>` 


Writing Commands
----------------

A command is ran with `kpm run <commandname> <arguments>`.

If you'd like to create a package that adds a new command to `kpm`, create a file `commands/__init__.py`:

```py
def register(subparsers):
	print("registering mycommand")
	parser = subparsers.add_parser('mycommand')
	parser.add_argument('thing')
	parser.add_argument('--feature', '-f', action="store_true", required=False)


def run_command(args):
	if args.command == 'mycommand':
		print(args.thing)
		print(args.feature)
```


Usage
-----

```bash
kpm init
kpm list
kpm search jlc
kpm show kpm-jlcpcb-basic
kpm install .
```

To add a new package to the package index, [submit a pull request](https://github.com/danroblewis/kicad-package-index)


### kpm.json
```json
{
	"name": "cool-project",
	"version": "0.0.1",
	"author": "danroblewis",
	"homepage": "http://githab.info/magic/stuff",
	"commands": {
		"test": "./fictional-spice-tester"
	},
	"dependencies": {
		"kpm-jlcpcb-basic": "0.0.5",
		"eurorack-parts": "0.0.1"
	}
}
```



Refresh Symbols and Footprints
------------------------------

After updating your libraries, the symbols/footprints in your schematic files won't have the latest changes. Do this to synchronize them:

* In `eeschema`, click `Tools > Update Symbols from Library...`, then save
* In `pcbnew`, click `Tools > Update Footprints from Library...`, then save

(If we can find a way to do this within kpm, that would be awesome.)



Package Directory Structure
---------------------------
```
/kpm.json

/symbols/
/symbols/mysymbols.kicad_sym

/footprints/
/footprints/myfootprints.pretty/
/footprints/myfootprints.pretty/myfootprints.kicad_mod

/3dmodels/
/3dmodels/something.step

/plugins/
/plugins/kicad-eurorack-tools/
/plugins/kicad-eurorack-tools/__init__.py

/simulation/
/simulation/mysim.spice

/sheets/
/sheets/mysubsheet.kicad_sch

/tests/
/tests/mytest.py

/scripts/
/scripts/mycommand.py
```
