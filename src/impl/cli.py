#!/usr/bin/python3
import argparse
        

__user_actions = {}

def define_user_action(function):
    __user_actions[function.__name__] = function
    return function

def get_user_action():
    global __user_actions
    
    parser = argparse.ArgumentParser()
    parser.add_argument('action', nargs=1, choices=__user_actions.keys())

    return __user_actions[parser.parse_args().action[0]]


    


