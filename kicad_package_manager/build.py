import os
import shutil
import zipfile


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))


def run_command(args):
	build_dir = 'build'
	if os.path.exists(build_dir):
		shutil.rmtree(build_dir)
	os.makedirs(build_dir)

	package_dirs = ['symbols', 'footprints']
	for package_dir in package_dirs:
		if os.path.exists(package_dir):
			print(package_dir, os.path.join(build_dir, package_dir))
			shutil.copytree(package_dir, os.path.join(build_dir, package_dir))
		else:
			print(f"no {package_dir}/ directory, skipping")
	shutil.copy('kpm.json', build_dir)

	with zipfile.ZipFile('package.zip', 'w', zipfile.ZIP_LZMA) as zh:
		zipdir(build_dir, zh)

