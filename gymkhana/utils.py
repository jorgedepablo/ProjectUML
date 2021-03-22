"""
Script that contents some functions for Gymkhana App extern to Django.

"""
import os 

def check_response(key, keyword): 
    keyword = str(keyword).lower()
    if keyword != key: 
        template = 'wrong.html'
    else:
        template = 'success.html'
    return template