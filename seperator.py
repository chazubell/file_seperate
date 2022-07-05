#! python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 04:40:05 2022

@author: E461183
"""

import sys
import re
import os
from os import walk
import shutil

regex = re.compile(r'^(?!\.)(.*)([-_ ](\(?\d+[a-z]?|_cover\d?(-clean)?|_sb)\)?\.(jpe?g|wmv|mp4|png))$',flags=re.IGNORECASE)

def get_folders(folder_name):
    

def get_command_line():
    folders = []
    if len(sys.argv) == 1:
        return None
    else:
        folders = sys.argv[1:]
        return folders


def split_file_name(fileName):
    if len(fileName) == 0:
        return (None, None)
    matches = re.match(regex, fileName)
    if matches == None:
        return (None, None)
    else:
        return matches.group(1), matches.group(2)


def collect_similar_names(folder_name):
    file_list = []
    keys = {}
    if os.path.isdir(folder_name):
        for (dirpath, dirnames, filenames) in walk(folder_name):
            file : str
            for file in filenames:
                match = re.match(regex, file)
                if match is not None:
                    file_list.append(file)
    elif os.path.isfile(folder_name):
        with open(folder_name) as f:
            file_list = f.readlines()
    else:
        return None

    for name in sorted(file_list):
        if name != None or len(name) > 0:
            # print(name)
            (root_name, suffix_file_name) = split_file_name(name)
            if keys.get(root_name) == None:
                keys[root_name] = []
                keys[root_name].append((name))
            else:
                keys[root_name].append((name))

    return keys


def create_dir_name(dir_name, path = '.'):
    '''
    Keyword Arguments
    :param dir_name: the name of the directory to be create
    :param path: the path where the director is to be created, default to the current directory
    :return: the path to the new directory
    '''
    count = 0
    tmp_dir_name = ""
    while True:
        try:
            os.mkdir(dir_name)
            break
        except FileExistsError:
            count += 1
            tmp_dir_name = '{0:s}_({1:2d})'.format(dir_name, count)
            dir_name = tmp_dir_name
    pwd = "{}/{}".format(path, dir_name)
    if pwd == "/":
        pwd = None
    return pwd


def move_to_folders(files: dict, path = '.'):
    moved_files = {}
    return_val = ""
    for key in files.keys():
        moved_files[key] = []
        directory = create_dir_name(key, path)
        '''
        if no directory created then just fill the array with None
        '''
        if directory is None:
            moved_files[key] = None
        else:
            file_names = files[key]
            for file in file_names:
                dst = directory
                try:
                    return_val = shutil.move(file, directory)
                except FileNotFoundError as event_str:
                    print("Error: When create directory {} error {} was thrown\n".format(directory, event_str) )
                # expected_value = "{}/{}".format(directory, file)
    return moved_files

def parse_files_create_folder(folder_name):
    folders_and_files = collect_similar_names(folder_name)
    move_to_folders( folders_and_files)


if __name__ == '__main__':

    files = get_command_line()
    if files == None:
        files[0] = os.getcwd()
    for file in files:
        os.chdir(file)
        dir = os.getcwd()
        keys = collect_similar_names(dir)
        move_to_folders(keys)



