# Testsuite_api

Launch :
```bash
$ python testsuite.py
```

## Yaml files 
### global parameters
First element is global parameters :
* Variables
* Headers (They will be added / replaced in all requests)

```yaml
- variables: {
    'name': 'foo',
  }
  headers: {
    'Content-Type' : 'application/json'
  }
```

### Requests
Following this, you have all your config requests.

**Mandatory fields** :

```yaml
- name: "[CATEGORY] This is a test"
  method: 'GET'
  url: 'http://localhost:8000'
  uri: "/my_uri"
  status_code: 200
```

**Optional fields** :

- *body*: 
You can add a **body** if it's a POST request.\
Values inside the body can be a global variable, then to get foo var write : "variable:foo".\
Otherwise directly write the value inside the body dictionnary.

```yaml
  body: {
    'name' : 'variable:name',
    'email' : 'foo@gmail.com',
  }
```
- *uri_var*: for variable in the uri\
Precise the variable to edit in the uri_var list. It will be update with global variables.


```yaml
  uri: "/my_uri/foo_id"
  uri_var: [
    'foo_id'
  ]
```

- *store_variable*: Store variable from the answer request body in the global variables.
```yaml
  store_variable: [
    'bar_token'
  ]
```


- *headers*: Add specific headers for a request\
Header values can be global variables.
```yaml
    headers: {
      'my_header_1' : 'variable:bar_token',
      'my_header_2' : 'XXX'
  }
```



