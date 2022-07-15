"""
Author: dizhong zhu
Date: 15/07/2022
"""
import subprocess
import os
import docker

if __name__ == '__main__':
    requirements_file = f'/requirements.txt'
    output_dir = '.build'
    python_version = '3.8'
    docker_folder = '/install_info'

    # client = docker.from_env()
    # a = client.containers.run(f'public.ecr.aws/sam/build-python{python_version}',
    #                           f'ls -lFa /',
    #                           f'pip install -r {docker_folder}/{requirements_file} -t {docker_folder}/{output_dir}/python',
    #                           volumes=[f'{os.getcwd()}:{docker_folder}']
    #                           )
    # print(a)

    subprocess.check_call([
        f'docker run --rm -v {os.getcwd()}:{docker_folder} public.ecr.aws/sam/build-python{python_version} /bin/sh -c '
        f'"pip install -r {docker_folder}/{requirements_file} -t {docker_folder}/{output_dir}/python;  '
        f'exit"'
    ], shell=True)
