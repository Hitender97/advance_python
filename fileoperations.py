import os

def read_content(file_name):
    with open (file_name,'r') as file:
        return file.readline()

def content_processing(data):
    return data.upper()

def write_updated_to_new_file(file_name,data):
    with open (file_name,'w') as file:
        file.writelines(data)



content=read_content('/home/xyz/input.txt')
content_upper = content_processing(content)
write_operation = write_updated_to_new_file('/home/xyz/output.txt',content_upper)

file_size = os.stat('home/xyz/output.txt')
print(f"file size in bytes of file output.txt {file_size.st_size}")