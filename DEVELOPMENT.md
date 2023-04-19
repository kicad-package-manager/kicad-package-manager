Project plan:

Step 1. Make `kpm init` and `kpm install` commands, config file format

Step 2. Make `kpm install` command work by explicit URL, github for now
	https://github.com/user/project/releases/download/v<version>/kpm.json




Packages to make:
- jlcpcb-smd-basics
	- all of the components in the jlcpcb library marked "basic"
- jlcpcb-smd
- jlcpcb-headers
- jlcpcb-connectors


use this to get list of parts:
https://github.com/yaqwsx/jlcparts




To release the package:

first, setup:
```bash
apt-get install python3.8-venv
pip3 install twine
```

to release:
```bash
python3 setup.py build && python3 setup.py upload
```



ToDo:
- kpm release command to increase packag version in kpm.json, build, and upload
- example .github/workflows
	https://github.com/ryanfobel/kicad-helpers/blob/main/.github/workflows/python-package.yml
	- should run release command
	- should tag commit and make github release with package.zip
- kpm generator for a package template

