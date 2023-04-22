import requests
import os
import json


repourl = "http://vps-407d02be.vps.ovh.us:80"


def run_command(args):
	if not os.path.exists('kpm.json'):
		print("no kpm.json file found")
		return

	with open('kpm.json') as f:
		kpmjson = json.loads(f.read())

	kpmrc_path = '.kpmrc'
	if not os.path.exists(kpmrc_path):
		kpmrc_path = os.path.expanduser('~/.kpmrc')
	if not os.path.exists(kpmrc_path):
		print("no .kpmrc directory found or ~/.kpmrc directory found")

	with open(kpmrc_path) as f:
		kpmrc = json.loads(f.read())

	if 'token' not in kpmrc:
		print("kpmrc does not have a 'token' field")
		return

	if 'name' not in kpmrc:
		print("kpmrc does not have a 'name' field")
		return

	pkgname = kpmjson['name']
	version = kpmjson['version']

	r = requests.put(f"{repourl}/package/{pkgname}/release/{version}", files={'file': open('package.zip', 'rb')})
	if r.status_code != 200:
		print(f"failed to upload file: {r.content}")
		return
	artifacturl = r.content.decode('utf-8').strip()


	r = requests.get(f"{repourl}/package/{pkgname}")
	if r.status_code == 404:
		pkgdata = {
			"name": pkgname,
			"owner": kpmjson['author'], 
			"homepage": kpmjson['homepage'],
			"releases": []
		}
	elif r.status_code == 200:
		pkgdata = r.json()
	else:
		print(f"server error {r.status_code}: {r.content}")


	new_release = {
		"version": version, 
		"artifact_url": artifacturl, 
		"author": kpmjson['author'],
		"dependencies": kpmjson['dependencies']
	}
	pkgdata['releases'].append(new_release)
	print(json.dumps(pkgdata, indent=4))
	r = requests.put(f"{repourl}/package/{pkgname}", json=pkgdata, headers={"Authorization": kpmrc['token']})
	print('status', r.status_code)
	print('content', r.content)

