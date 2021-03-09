import os
from os import path
import shutil

dirs = os.walk("my_project")
target_dir = r"my_project\templates"
if not path.exists(target_dir):
	os.makedirs(target_dir)
for i in dirs:
	print(i)
	if 'templates' in i[0] and i[2] and target_dir not in i[0]:
		print("in dirs")
		temp_app_dir = path.basename(i[0])
		for file in i[2]:
			file_1 = path.join(i[0], file)
			print(file_1)
			if not path.exists(path.join(target_dir, temp_app_dir)):
				os.makedirs(path.join(target_dir, temp_app_dir))
			shutil.copy(file_1, path.join(target_dir, temp_app_dir))
