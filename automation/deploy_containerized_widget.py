import os,sys,threading,asyncio,re,json

#get image, image_id

#Initital container should have compose installed
#async def create_base_container(setup_image):

#async def setup_env(self):
class d():
    def __init__(self):
        print('begin')
        self.container_image_id = ''
        self.container_id = ''
        self.net_id = ''


    async def generate_app_run_cmd(self, docker_net_name, app_name, db_name):
        statement_ = f"""
          docker run -dp 3000:3000 \
            -w /{app_name} \
            -v "app:/{app_name}" \
            --network {docker_net_name} \
            -e MYSQL_HOST=mysql \
            -e MYSQL_USER=root \
            -e MYSQL_PASSWORD=secret \
            -e MYSQL_DB={db_name} \
            ubuntu:latest \
            sh -c echo "yarn install && yarn run dev"
            """
        return statement

    async def generate_db_run_cmd(self, docker_net_name, app_name, db_name):
        statement_ = f"""
              docker run -d \
              --network todo-app --network-alias mysql \
              -v todo-mysql-data:/var/lib/mysql \
              -e MYSQL_ROOT_PASSWORD=secret \
              -e MYSQL_DATABASE= \
              mysql:5.7
            """
        return statement

    async def start_db_container(self, docker_net_name):
        return None
    async def generate_compose(self, os, version, purpose, ports, cmds):
        compose_command = ''
        for c in cmds:
            compose_command += '\t'+ c +'\n'
        #yml.
        statement_ = f"""
    ---
    version: '3.7'
    services:
    app:
    image: {os}
    container_name: test_container
    working_dir: /home
    volumes:
      - "./scripts:/home"

    ports:
      - 2500:2500
    # Default command used when running `docker compose up`
    command: >
      {compose_command}
    """

        with open('./docker-compose.yml', 'w+') as compose:
            compose.write(statement_)
        print('compose file success')

    async def init_container_env(self, os, install_cmd, init_cmds, shell_flag, container_name, utils):
        flag = False
        try:
            if flag:
                for c in init_cmds:
                    print(f"Attempting {init_cmds[c]}")
                    cmd_ = f'sudo docker exec -d -t {container_name} {init_cmds[c]}'
                    print(cmd_)
                    execute_cmd = await asyncio.create_subprocess_shell(f'sudo docker exec -t {container_name} {init_cmds[c]}',
                                                                        stdout = asyncio.subprocess.PIPE,
                                                                        stderr = asyncio.subprocess.PIPE
                                                                        )
                    stdout, stderr = await execute_cmd.communicate()
                    string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
                    string_of_stderr = str(f'[stderr]\n{stderr.decode()}')
                    lines = re.split(r'\n', string_of_stdout)
                    if stdout:
                        print(string_of_stdout)
                        print(f"{c} installed")
                    if stderr:
                        print(f"Command failed setup: {e} \n OS: {os}\n\n", end=" ", file=open('failedcmds.txt', 'a'))

                for u in utils:
                    print(f"Attempting {utils[c]}")
                    #filter by os
                    execute_util = await asyncio.create_subprocess_shell(f'sudo docker exec -t {container_name} {install_cmd} -y {utils[u]}',
                                                                        stdout = asyncio.subprocess.PIPE,
                                                                        stderr = asyncio.subprocess.PIPE
                                                                        )
                    stdout, stderr = await execute_util.communicate()
                    string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
                    string_of_stderr = str(f'[stderr]\n{stderr.decode()}')
                    lines = re.split(r'\n', string_of_stdout)
                    if stdout:
                        print(string_of_stdout)
                        print(f"{u} installed")
                        continue
                    if stderr:
                        print(f"Command failed during environment setup: {e} \n OS: {os}\n\n", end=" ", file=open('failedcmds.txt', 'a'))
                        continue
            #Shell
            shell_flag = await asyncio.create_subprocess_shell(f'sudo docker exec -t {container_name} bash ./test_setup.sh {shell_flag}',
                                                                stdout = asyncio.subprocess.PIPE,
                                                                stderr = asyncio.subprocess.PIPE
                                                                )
            stdout, stderr = await shell_flag.communicate()
            string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
            string_of_stderr = str(f'[stderr]\n{stderr.decode()}')
            lines = re.split(r'\n', string_of_stdout)
            if stdout:
                print(string_of_stdout)
                print("Flag success")
            if stderr:
                print(f"Command failed during environment setup: {e} \n OS: {os}\n\n", end=" ", file=open('failedcmds.txt', 'a'))
            #stop container
            #For testing
            #stop_ = await asyncio.create_subprocess_shell(f'sudo docker stop {container_name}',
            #                                                    stdout = asyncio.subprocess.PIPE,
            #                                                    stderr = asyncio.subprocess.PIPE
            #                                                    )
            #if stdout:
            #    print(string_of_stdout)
            #    print("Container stopped")
            #if stderr:
            #    print(f"Failed to stop container", end=" ", file=open('failedcmds.txt', 'a'))


            print('#-------------------env setup complete-------------------#')

        except Exception as e:
            print(e)
        return

    async def setup_container(self, containerd, purpose, utils, shell_path):
        success=False
        #self.containerd = containerd
        os = containerd["os"]
        version = containerd["version"]
        container_name = containerd["tag"] + "_" + purpose
        port = containerd["port"]
        setup_path = shell_path

        get_ = {
            "get_version":f"sudo docker pull {os}:{version}",
            #Regex stdout
            "get_image_id":"sudo docker image ls",
            #"run": f"sudo docker run -d {image_id}"
            "get_container_id":"sudo docker ps -a"
        }
        try:
            for g in get_:
                 print(str(get_[g]))
                 begin = await asyncio.create_subprocess_shell(str(get_[g]),
                                                                    stdout=asyncio.subprocess.PIPE,
                                                                    stderr=asyncio.subprocess.PIPE
                                                                    )
                 stdout, stderr = await begin.communicate()
                 string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
                 lines = re.split(r'\n', string_of_stdout)
                 if stdout and g=='get_image_id':
                     #fetch image id
                     for line in lines:
                         if os and version in line:
                             print(line)
                             self.container_image_id = re.findall(r'(?:[0-9a-z]){12}', line)[0]
                             print(self.container_image_id)
                             #run suspended
                             rs = await asyncio.create_subprocess_shell(f'sudo docker run --name {container_name} -dp {port} -t --rm {self.container_image_id}',
                                                                        stdout=asyncio.subprocess.PIPE,
                                                                        stderr=asyncio.subprocess.PIPE
                                                                        )
                             stdout, stderr = await rs.communicate()
                             if stdout:
                                 #string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
                                 print("\n\n#-----------------------container running-------------------------#\n\n" + str(f'[stdout]\n{stdout.decode()}'))
                             if stderr:
                                 print('setup_container failed:' + str(f'[stderr]\n{stderr.decode()}'))


                 if stdout and g=='get_version':
                     string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
                     print(string_of_stdout)

                 if stdout and g=='get_container_id':
                     for line in lines:
                         print(line)
                         if self.container_image_id in line:
                             print('match')
                             self.container_id = re.findall(r'(?:[0-9a-z]){12}', line)[0]
                             print(f'{self.container_image_id}: {self.container_id}')

                 if stderr:
                     print(f'get_container_id failed: [stderr]\n{stderr.decode()}')

            #Transfer sh
            tr = await asyncio.create_subprocess_shell(f'sudo docker cp {setup_path} {container_name}:/',
                                                    stdout=asyncio.subprocess.PIPE,
                                                    stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await tr.communicate()
            if stdout:
                string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
                print("\n\n#-----------------------Shell script transported-------------------------#\n\n" + str(f'[stdout]\n{stdout.decode()}'))
                #can't make a task?
            if stderr:
                print('Setup script transport fail:' + str(f'[stderr]\n{stderr.decode()}'))

            setup_container_env = await asyncio.create_task(self.init_container_env(os, containerd["install_cmd"], containerd["init_cmds"], containerd["shell_flag"], container_name, utils))
            print(setup_container_env)
            print(f"Env setup complete for {os}:{version}")
        except Exception as e:
            print(e)
            exit(1)

    async def init_docker_net(self, base_container_image,  docker_net_name):
        net_ = {
            #"prune_docker": 'sudo docker system prune',
            "init_net": f"sudo docker network create {docker_net_name}"
        }

        for n in net_:
            init_net = await asyncio.create_subprocess_shell(str(net_[n]),
                                                            stdout = asyncio.subprocess.PIPE,
                                                            stderr = asyncio.subprocess.PIPE
                                                            )
            stdout, stderr = await init_net.communicate()
            string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
            string_of_stderr = str(f'[stderr]\n{stderr.decode()}')
            lines = re.split(r'\n', string_of_stdout)
            if stdout and n == 'init_net':
                self.net_id = string_of_stdout.replace(' ', '')
                cluster_init = await asyncio.create_task(self.create_base_container(self.net_id, base_container_image))
            if stderr:
                print('Net init failed' + string_of_stderr)
                exit(1)

    async def deploy_cluster(self, docker_net_name, net_id, db_name, base_container_image):
        #scripts/setup_docker_net.sh -ac
        version = 'latest'
        _service = {
            "init_db_service": f'docker run -d --network {net_name} --network-alias mysql -v todo-mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=todos mysql:5.7 sh -c echo "db_service test success"',
            "init_app_service": f'docker run -dp 3000:3000 -w /app -v "$(pwd):/app" --network {net_name} -e MYSQL_HOST=mysql -e MYSQL_USER=root -e MYSQL_PASSWORD=secret -e MYSQL_DB=<> ubuntu:latest sh -c echo "app_service test success',
            "compose-up": f'docker-compose up -d'
        }
        for d in _service:
            try:
                 send = await asyncio.create_subprocess_shell(str(_service[d]),
                                                                    stdout=asyncio.subprocess.PIPE,
                                                                    stderr=asyncio.subprocess.PIPE
                                                                    )
                 stdout, stderr = await send.communicate()
                 string_of_stdout = str(f'[stdout]\n{stdout.decode()}')
                 lines = re.split(r'\n', string_of_stdout)
                 if stdout:
                     print(str(f'[stdout]\n{stdout.decode()}'))
                 if stderr:
                     print(str(f'[stderr]\n{stdout.decode()}'))
                #generate compose
                 template = f'''
version: "3.7"
services:
  app:
    image: {base_container_image}/{latest}
    command: sh -c "yarn install && yarn run dev"
    ports:
      - 3000:3000
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: todos

  mysql:
    image: mysql:5.7
    volumes:
      - data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: tmp_pass
      MYSQL_DATABASE: {net_name}

volumes:
  todo-mysql-data:'''
                 with open('docker-compose.yml', 'w+') as compose_file:
                     compose_file.write(template)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    quest_ = {
        #if state for "util" can have multiple
        #testing to install utils set flag=True
        "shell_path" : "~/Documents/setup/docker/test_setup.sh",
        "utils" : {
            "python" : "python3.8.13",
            "pip" : "python3-pip",
        },
        #String replacement for tag_
        "containers":[
        {
        "purpose": "db",
        "os" : "debian",
        "version": "stable",
        "port": "2600:2600",
        "tag" : "sql_pylon",
        "install_cmd": "apt install",
        "shell_flag": "--docker_run_jupyterlab",
        "init_cmds" : {
                "update" : "apt-get update"
            }
        },
        {
        "purpose": "jupyterlab",
        "os" : "ubuntu",
        "version": "18.04",
        "port": "2660:2660",
        "tag" : "jupyterlab_pylon",
        "install_cmd": "apt install",
        "shell_flag": "--docker_run_jupyterlab",
        "init_cmds" : {
                "update" : "apt-get update"
            }
        },
        {
        "purpose": "api",
        "os" : "ubuntu",
        "version": "18.04",
        "port": "2680:2680",
        "tag" : "api_pylon",
        "install_cmd": "apt install",
        "shell_flag": "--prop_api_test",
        "init_cmds" : {
                "update" : "apt-get update"
            }
        },
        ],
    }
    for containerd in quest_['containers']:
        test = d()
        container_id = asyncio.run(test.setup_container(containerd, quest_["purpose"], quest_["utils"], quest_["shell_path"]))
    exit(0)

#async def compose_app(base_container_id):
