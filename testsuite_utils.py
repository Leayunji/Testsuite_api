import yaml
import json
from typing import Dict, List, Any


""" = = = = = = = = =
        UPDATES
= = = = = = = = = """

def update_value(value: str, global_variables: Dict) -> Any:
    """
        Update a value with global_variables dictionnary
        example:
        'variable:name' -> global_variables[name] -> 'foo'
    """
    if ('variable:' in value):
        variable_name = value.replace('variable:', '')
        variable_value = global_variables.get(variable_name, '')
        return variable_value
    else:
        return value

def update_global_variables(req: Dict, body: str, global_variables: Dict):
    """
        Update the global_variables dictionnary if there is variables to keep from the answer request.
        Check 'store_variable' in the request yaml config
    """
    store_var = req.get('store_variable', {})

    for var in store_var:
        print('[STORE_VAR] {} : {}'.format(var, body.get(var)))
        global_variables[var] = body.get(var)
    
    return global_variables




""" = = = = = = = = =
       BUILDERS
= = = = = = = = = """


def build_url(request: Dict, global_variables: Dict) -> str:
    """
        build the full URL from yml config and global variables
        ex : url/uri/account_id
        -> https::localhost:8000/create_account/9876dfheid8
    """

    url = request.get('url')
    uri = request.get('uri', '')

    # replace variables in uri
    uri_var = request.get('uri_var', [])
    for var in uri_var:
        # get value from globale variables
        value = global_variables.get(var, '')
        uri = uri.replace(var, value)

    return f'{url}{uri}' 

def build_body(request: Dict, global_variables: Dict):
    body = {}
    body_content = request.get('body', {})

    for key, value in body_content.items():
        # update value of body if it's in global variables
        body[key] = update_value(value, global_variables)

    return body

def build_headers(request: Dict, global_variables: Dict, global_headers: Dict):
    headers = request.get('headers', {})

    for key, value in headers.items():
        # update value of header if it's in global variables
        headers[key] = update_value(value, global_variables)
    # add global headers
    headers.update(global_headers)

    return headers

  