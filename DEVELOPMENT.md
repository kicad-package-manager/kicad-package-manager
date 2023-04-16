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
python -m twine upload --repository kicad-package-manager dist/*
```