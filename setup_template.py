import os
import pathlib
import glob
import shutil

from jinja2 import Environment, FileSystemLoader, meta, Template


def get_variables(filename):
	env = Environment(loader=FileSystemLoader('.'))
	template_source = env.loader.get_source(env, filename)[0]
	parsed_content = env.parse(template_source)
	return meta.find_undeclared_variables(parsed_content)


def main():

	deploy_folder = input("Deploy folder: ")

	file_list = []
	for filename in glob.iglob('./**/*', recursive=True):
		if __file__ not in filename:
			file_list.append(filename)
	for filename in glob.iglob('.**/*', recursive=True):
		if ".git/" not in filename:
			file_list.append(filename)

	tag_dict = dict()
	for i, file_name in enumerate(file_list):

		pathlib.Path("{}/{}".format(
			deploy_folder,
			"/".join(file_name.replace("./", "").split("/")[:-1])
		)).mkdir(parents=True, exist_ok=True)

		dest_file_name = "{}/{}".format(deploy_folder, file_name.replace("./", ""))

		print("====== {} -> {} ======".format(file_name, dest_file_name))

		try:
			jinja_var_list = get_variables(file_name)
		except Exception as e:
			print(e)
			if os.path.isfile(file_name):
				shutil.copyfile(file_name, dest_file_name)
			continue

		for idx, tag in enumerate(jinja_var_list):
			if tag not in tag_dict:
				new_value = input("{}: ".format(tag))
				if new_value == "":
					new_value = "[[{}]]".format(tag)
				tag_dict[tag] = new_value
			else:
				print("{} already set!".format(tag))
		with open(file_name, "r") as f_in:
			content = f_in.read()

			t = Template(content)
			new_content = t.render(**tag_dict)
			with open(dest_file_name, "w") as f_out:
				f_out.write(new_content)
	return


if __name__ == '__main__':
	main()
