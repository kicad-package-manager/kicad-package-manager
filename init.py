
import config
import os

def run_command(args):
	# create empty json file

	c = config.Config()

	with open('kpm.json', 'w') as f:
		f.write(c.to_json())

	if os.path.exists('.gitignore'):
		with open('.gitignore') as fr:
			if 'kpm_modules' not in fr.read():
				with open('.gitignore', 'a') as fw:
					fw.write("\nkpm_modules")
	else:
		with open('.gitignore', 'w') as f:
			f.write("kpm_modules\n")


