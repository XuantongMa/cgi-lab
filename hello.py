#!/usr/bin/env python3

import os
import json
from templates import login_page, secret_page, after_login_incorrect, _wrapper

# create an empty dictionary
env = {}

# Iterate through environment variables and add them to env
for env_key, env_value in os.environ.items():
    env[env_key] = env_value
    #print('{} -> {}'.format(env_key,env_value))

'''
print("Content-Type: application/json")
print()                               

# Print env dictionary in json format
print(json.dumps(env))
'''
print("Content-Type: text/html")
print()
print("<!doctype html><title>Hello</title><h2>Hello</h2>")
print(os.environ["QUERY_STRING"])
print()
print(os.environ["HTTP_USER_AGENT"])
print(login_page())