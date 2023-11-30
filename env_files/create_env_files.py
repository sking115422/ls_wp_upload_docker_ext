import os
import random

num_cont = 5
start_ssh_port = 65201
start_web_port = 65401
rand_seed = random.randint(1, 1000)

with open("./rand_seed.txt", "w+") as file:
    file.write(str(rand_seed))

for i in range(0, num_cont):

    txt = f"""
### DOCKER LS UPLOAD CONT ENV FILE

# Server Access Information

# usr: spencer
LS_DOCKER_USR=admin

# host: faraday.cs.uga.edu
# host: 128.192.193.150
LS_DOCKER_HOST=maxwell.cs.uga.edu

# pass: Spencer.2328
LS_DOCKER_PASS=adminpass544002
# LS_DOCKER_PASS=none

# key_path: ~/.ssh/ls-gen-cont-docker
# LS_DOCKER_KEY_PATH=/home/spenc/.ssh/ls_gen_cont
LS_DOCKER_KEY_PATH=none

# Host port
# port: 8801  
LS_DOCKER_HOST_PORT={start_web_port + i}

# SSH port
# cont_port: 2201  
LS_DOCKER_SSH_PORT={start_ssh_port + i}

# Label Studio Access Information

# Test token
# token: Token fd7f8c1755de53c9993729ae9d2b029b2622621a
# Gen container token
# token: Token eee2e2a1eb1a4b842e3cdaaf9e04e6d75313c5c7
# Maxwell Token
LS_DOCKER_TOKEN="Token a327d1ca1bd2fde45dfbc25d2765cb370cd21418"

# Upload Parameters
upload_parameters:

LS_DOCKER_UPLOAD_SS_BATCH_SIZE=10
LS_DOCKER_UPLOAD_JSON_BATCH_SIZE=10
LS_DOCKER_GT_ELEM_PER=.5
LS_DOCKER_GT_SEED={rand_seed}
# Total number uploads minus number of ground truth images
# Total = 20
# Ground Truths = 3
# max_upload_num = 20 - 3 = 47 + 1 > for (approximately exact upload)
LS_DOCKER_MAX_UPLOAD_NUM=50

# Puppeteer Configurations

LS_DOCKER_VIEW_HEIGHT=1080
LS_DOCKER_VIEW_WIDTH=1920
LS_DOCKER_TIME_OUT_SEC=30
LS_DOCKER_DELAY_MS=5000
LS_DOCKER_WAIT_UNTIL=networkidle2
LS_DOCKER_HEADLESS=new


### Paths Used In the Web_Crawler Code
# Local paths to hold data locally during the transfer process

# Path for raw data output from initial web crawl
LS_DOCKER_SITE_DATA_REL=./site_data/
# Path for data converted from original site data
LS_DOCKER_LS_DATA_REL=./ls_data/

#####################################################################################

### Server Upload Paths
# Path below MUST NOT end in a "/"
# API path to import tasks
LS_DOCKER_SERVER_LS_IMPORT_API=/api/projects/1/import
# API path to get tasks
LS_DOCKER_SERVER_LS_TASKS_API=/api/projects/1/tasks
# All paths below MUST end with "/"
# Server path for webpage screen shots to be stored
LS_DOCKER_SERVER_LS_SS_PATH=/home/spencer/label_studio/data/ss/user/
# Server path so that label studios can find images associated with each json file
LS_DOCKER_SERVER_LS_JSON_SS_LINK_PATH=label_studio/data/ss/user/

#####################################################################################

### Ground Truth Path
# Upload ground truth ss
LS_DOCKER_GT_UPLOAD=true
LS_DOCKER_GT_DIR=/mnt/uploads/gt_data/

### General Upload Paths
# Upload new ss
LS_DOCKER_NEW_SS_IMG=true
# Below determines whether the code will use mhtml from a directory or urls listed as line items in a file
# Source type can either by "url" or "mhtml"
LS_DOCKER_SOURCE_TYPE=url
# Fill in path to mhtml directory below if applicable
LS_DOCKER_MHTML_DIR=C:/Users/spenc/Desktop/doc_res/WebApp_PageLabeling/upload_mhtml/
# Fill in path to url file below if applicable
# Last uploaded f_3
LS_DOCKER_URL_PATH=/mnt/uploads/upload_url/f_{10000 - i}.txt
    """
# LS_DOCKER_URL_PATH=/mnt/uploads/upload_url/f_{i + 1}.txt

    with open(f"./ls_docker_env_file_" + str(i+1) + ".txt", "w+") as f:
        f.write(txt)
    