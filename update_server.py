
def update_server_file(path,key,value):
    with open (path,"r") as file:
        file_data = file.readlines()

    with open (path,"w") as file:
        for line in file_data:
            if key in line:
                file.write(key + "=" + value +"\n")
            else:
                file.write(line)


server_config_path = "/home/hitender_p/vscode_work/python4devops/server.conf"
key_to_update = "MAX_CONNECTIONS"
required_new_value = "5000"

update_server_file(server_config_path,key_to_update,required_new_value)