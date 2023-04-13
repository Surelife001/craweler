import os

# Each website you crawl is a seperate project (Folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project" + directory)
        os.makedirs(directory)


# create queue and crawled file (if not created)
def create_data_file(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")




# create a new file
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()

# add adata onto an existing file
def append_to_file(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")

# delete the content of a file
def delete_file_content(path):
    with open(path, "a"):
        pass


#  read a file and convert each line to set()
def file_to_set(file_name):
    result = set()
    with open(file_name, "r") as f:
        for line in f:
            result.add(line.replace("\n", ""))
    return result


# iterate through a set, each item will be new line in the file
def set_to_file(links, file):
    delete_file_content(file)
    for link in links:
        append_to_file(file, link)






