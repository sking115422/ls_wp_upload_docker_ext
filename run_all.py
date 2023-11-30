import os

cont_list = [1, 2, 3, 4, 5]

def getCMD(cont_num):
    
    port = 52200 + cont_num
    
    docker_cmd = f"""
    docker run --rm -d -i -t \
    -v /home/spenc/nis_lab_research/docker_ls_uploader/wp_upload_vol:/mnt/uploads \
    -p {port}:22 \
    --cpus="4.0" \
    --memory="8G" \
    --name ls_upload_cont_{cont_num} \
    --hostname ls_upload_cont_{cont_num} \
    --entrypoint "./startup.sh" \
    --env-file ./env_files/ls_docker_env_file_{cont_num}.txt \
    sking115422/ls_upload_cont:v3 /bin/bash \
    """
    
    return docker_cmd

cmd_list = []

for cont_num in cont_list:
    cmd_list.append(getCMD(cont_num))
    
all_cmd = " & ".join(cmd_list)

# print(all_cmd)

os.system(all_cmd)