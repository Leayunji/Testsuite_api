import yaml
import json
from typing import Dict, List, Any
import os

import testsuite_utils as utils
          

def request_get(url: str, headers: Dict):
    print(f'[GET] {url}')
    print('headers', headers)    
    # FIXME : return real get request

def request_post(url: str, body: str, headers: Dict):
    print(f'[POST] {url}')
    print('body: ', body)
    print('headers', headers)
    # FIXME : return real post request


def launch_test_session(requests: List, global_variables: Dict, global_headers: Dict):
    for req in requests:
        print(req['name'])

        # Build URL
        url = utils.build_url(req, global_variables)
        # Build Headers
        headers = utils.build_headers(req, global_variables, global_headers)

        # Check method
        method = req.get('method')
        if method == 'GET':
            answer =request_get(url, headers)
        elif method == 'POST':
            # Build body
            body = utils.build_body(req, global_variables)
            answer = request_post(url, body, headers)
        else:
            print(f'Method not implemented : {method}')

        # FIXME answer.body// get the body of answer request
        # FIXME fake body
        answer_body = {'token' : '09876fer5WWWZKJD', 'account_id' : '63kfrdnd', 'config_id' : '55555'}

        global_variables = utils.update_global_variables(req, answer_body, global_variables)

        # FIXME : answer.status_code >> check status code
        print('\n',' - ' * 10)


def load_yaml_and_launch_test(path: str):
    print('\n','-' * 5, f'[LAUNCH] {path}', '-' * 5, '\n')
    with open(path, 'r') as file:
        yaml_content = yaml.safe_load(file)

    config = yaml_content[0]
    global_variables = config.get('variables', {})
    global_headers = config.get('headers', {})

    print('VARIABLES', global_variables)
    print('HEADERS', global_headers)
    print('-' * 10, '\n')

    requests = yaml_content[1:]
    launch_test_session(requests, global_variables, global_headers)

if __name__ == '__main__':
    # FIXME : Get path by arg
    yml_path = 'yaml_files'

    # Loop over all yaml files
    for yml_file in os.listdir(yml_path):
        # Check if it's a Yaml file
        if yml_file.endswith(".yaml"):
            path = os.path.join(yml_path, yml_file)
            load_yaml_and_launch_test(path)


