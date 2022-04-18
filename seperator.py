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

regex = re.compile(r'^(?!\.)(.*)(_(\(?\d+|_cover(-clean)?)\)?\.(jpg|wmv|mp4|jpeg))$')


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


def create_dir_name(dir_name):
    count = 0
    tmp_dir_name = ""
    if os.path.isdir(dir_name):
        while os.path.isdir(dir_name):
            count += 1
            tmp_dir_name = r'{0:s}_({1:2d})'.format(dir_name, count)
        dir_name = tmp_dir_name
    pwd = os.getcwd() + r'\\'
    pwd += dir_name
    return os.mkdir(pwd)


def move_to_folders(files: dict):
    moved_files = {}
    return_val = ""
    for key in files.keys():
        moved_files[key] = []
        directory = create_dir_name(key)
        if directory is None:
            moved_files[key] = None
        else:
            file_names = files[key]
            for file in file_names:
                dst = directory
                return_val = shutil.move(file, directory)
                expected_value = "{}/{}".format(directory, file)
                if return_val != expected_value:
                    moved_files[key].append(None)
                else:
                    moved_files[key].append(return_val)
    return moved_files

def parse_files_create_folder(folder_name):
    folders_and_files = collect_similar_names(folder_name)
    move_to_folders(folders_and_files)

if __name__ == '__main__':
    file = "foo.txt"
    #pwd = os.getcwd()
    #os.chdir(pwd)
    # pwd += '\\' + 'foo.txt'
    keys = collect_similar_names(file)
    move_to_folders(keys)



