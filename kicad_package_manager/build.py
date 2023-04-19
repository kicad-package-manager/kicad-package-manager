import os
import shutil
import zipfile


def init_command(parser):
    parser.add_argument('--keep-build-dir', '-k', action="store_true", required=False)


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            from_path = os.path.join(root, file)
            to_path = os.path.relpath(os.path.join(root, file), os.path.join(path, '..')).replace(path + "/","",1)
            print("adding", from_path)
            ziph.write(from_path, to_path)


def run_command(args):
    build_dir = 'build'
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)

    package_dirs = ['symbols', 'footprints', 'subsheets', 'commands']
    for package_dir in package_dirs:
        if os.path.exists(package_dir):
            shutil.copytree(package_dir, os.path.join(build_dir, package_dir))
        else:
            print(f"no {package_dir}/ directory, skipping")
    shutil.copy('kpm.json', build_dir)

    with zipfile.ZipFile('package.zip', 'w', zipfile.ZIP_LZMA) as zh:
        zipdir(build_dir, zh)

    if not args.keep_build_dir:
        shutil.rmtree(build_dir)

