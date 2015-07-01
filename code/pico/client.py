"""
Load and call functions from a remote pico module.

pico.client.url = "http://localhost:8800/pico/" # the url of the remote pico server
example = pico.client.load('example')
s = example.hello()
# s == "Hello World"

s = example.hello("Python")
# s == "Hello Python"

Use help(example.hello) or example.hello? as normal to check function parameters and docstrings.
"""

__author__ = 'Fergal Walsh'
__version__ = '1.2.0'

import urllib
import urllib2
import json
import imp
import time
import hashlib
import httplib
import pico

url = 'http://localhost:8800/pico/'
_username = None
_password = None
_td = 0

def get(url, args={}, stream=False):
    if _username:
        args['_username'] = _username
        args['_nonce'] = int(time.time()) + _td
        args['_key'] = _hash(_password + str(args['_nonce']))
    encoded_args = urllib.urlencode(args)
    if stream:
        return _stream(url, encoded_args)
    else:
        r =  urllib.urlopen(url, encoded_args).read()
        data = json.loads(r)
        if type(data) == dict and 'exception' in data:
            raise Exception(data['exception'])
        else:
            return data

def _stream(url, encoded_args=""):
    s = urllib2.urlparse.urlsplit(url)
    try:
        c = httplib.HTTPConnection(s.netloc)
        u = s.path + '?'
        if s.query: u += s.query + '&'
        u += encoded_args
        c.request("GET", u)
        r = c.getresponse()
        for l in r.fp:
            if 'data:' in l:
                yield json.loads(l[6:-1])
    finally:
        c.close()


def _call_function(module, function, args, stream=False): 
    for k in args:
        args[k] = pico.to_json(args[k])
    # args['_function'] = function
    # args['_module'] = module
    return get(url + '%s/%s/'%(module, function), args, stream)

def authenticate(username, password):
    """ 
    Authenticate with the pico server

    You must call this function before calling any protected functions.
    """
    global _username
    global _password
    _username = username
    _password = _hash(password)
    try:
        r = _call_function('pico', 'authenticate', locals())
        return True
    except Exception, e:
        r = str(e)
        if r.startswith('Bad nonce.'):
            global _td
            _td = int(r.split('Bad nonce. The time difference is:')[-1])
            print(r)
            authenticate(username, password)
        else:
            print(r)
    return False

def unauthenticate():
    global _username
    global _password
    _username = None
    _password = None
    return True

def load(module_name):
    """ 
    Load a remote module 
    pico.client.url must be set to the appropriate pico url first.
    e.g. pico.client.url="http://localhost:8800/pico/"

    example = pico.client.load("example")
    """
    if module_name.startswith('http://'):
        pico_url, module_name = module_name.split('/pico/')
        global url
        url = pico_url + '/pico/'
    module_dict = get(url + module_name)
    module = imp.new_module(module_name)
    module.__doc__ = module_dict['__doc__']
    functions = module_dict['functions']
    for function_def in functions:
        name = function_def['name']
        args = function_def['args']
        args_string = ', '.join(["%s=%s"%(arg, json.dumps(default).replace("null", "None")) for arg, default in args if arg != None])
        stream = function_def['stream']
        docstring = function_def['doc']
        exec("""
def f(%s):
    \"\"\" %s \"\"\"
    return _call_function('%s', '%s', locals(), %s)
"""%(args_string, docstring, module_name, name, stream))
        setattr(module, name, f)
    return module

def _hash(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()
    