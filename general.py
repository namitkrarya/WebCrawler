import os

#creating folder(project)
def create_project(directory):
	if not os.path.exists(directory):
		print('Creating project ' + directory )
		os.makedirs(directory)

# creating data files
def create_files(directory, base_url):
	queue = os.path.join(directory, 'queue.txt')
	crawled = os.path.join(directory, 'crawled.txt')
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

#write a file
def write_file(path, data):
	with open(path, 'w') as f:
		f.write(data)

#add content to file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')

#make file empty
def delete_file_content(path):
	open(path, 'w').close()

# read a file and convert each line to set items
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
	with open(file, 'w') as f:
		for link in sorted(links):
			f.write(link + '\n')




