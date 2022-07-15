"""
Author: dizhong zhu
Date: 15/07/2022
"""
import subprocess
import os

if __name__ == '__main__':
    requirements_file = f'/requirements.txt'
    output_dir = '.build'
    python_version = '3.8'
    docker_folder = '/install_info'

    subprocess.check_call([
        f'docker run --rm -v {os.getcwd()}:{docker_folder} public.ecr.aws/sam/build-python{python_version} /bin/sh -c '
        f'"pip install -r {docker_folder}/{requirements_file} -t {docker_folder}/{output_dir}/python;  '
        f'exit"'
    ], shell=True)
