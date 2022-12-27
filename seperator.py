#! /usr/local/bin/python3
#   ! ddpython3
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

regex = re.compile(r'^(?!\.)(.*?)([-_ ](\(?\d+[a-z]?|_cover\d?(-clean)?|_sb|_AA|[\w+])\)?\.(jpe?g|wmv|mp4|png))$' ,
                   flags=re.IGNORECASE)
regex2 = re.compile(r'^(.*)_(\d+)\.jpe?g$')


def distinguish_files(file_list_singleton: dict):
    """
    The function was created because some list_of_files are only distinguished by the discontinuity of
    sequencing of the file names
    :param file_list_singleton: a dictionary with only a single value
    :return: dictionary with directory names as keys and a list of file names
    """
    if not len(file_list_singleton.keys()) == 1:
        return None
    list_of_files = list(file_list_singleton.values())[0]
    list_of_files = sorted(list_of_files)

    distinguished_names = {}
    counter = 1  # used to name folders
    i = 0  # an index
    while i < len(list_of_files):

        current_file = list_of_files[i]
        match1 = re.match(regex2 ,current_file)
        if match1 is None:
            i += 1
            continue
        else:
            file_index1 = match1.group(2)
        new_name = '{0}_{1:05d}'.format(match1.group(1) ,counter)
        if i <= len(list_of_files)-2:
            next_file = list_of_files[i + 1]
            match2 = re.match(regex2 ,next_file)
            if match2 is None:
                i += 2
                continue
            else:
                file_index2 = match2.group(2)

            if new_name not in distinguished_names.keys():
                distinguished_names[new_name] = []
            if not is_contiguious(int(file_index1), int(file_index2)):
                counter += 1
                newer_name = '{0}_{1:05d}'.format(match2.group(1) ,counter)
                distinguished_names[newer_name] = []
        i += 1
        distinguished_names[new_name].append(current_file)
    return distinguished_names


def get_command_line():
    """
    check the value of the command line
    :return: empty list
    """
    folders = []
    if len(sys.argv) == 1:
        return folders
    else:
        folders = sys.argv[1:]
        return folders


def split_file_name(file_name):
    if len(file_name) == 0:
        return None ,None
    matches = re.match(regex ,file_name)
    if matches is None:
        return None ,None
    else:
        return matches.group(1) ,matches.group(2)


def collect_similar_names(folder_name):
    """
        Given a list of files name collect all the files that have names that are similar up to
        the enumeration at the end of the files name (excluding the extension

        Param: List of file names
        Returns a dict of folder names and files that go into the folder
    """
    file_list = []
    folders_and_files = {}
    if os.path.isdir(folder_name):
        for (dirpath ,dirnames ,filenames) in walk(folder_name):
            file: str
            for file in filenames:
                match = re.match(regex ,file)
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
            (root_name ,suffix_file_name) = split_file_name(name)
            if folders_and_files.get(root_name) == None:
                folders_and_files[root_name] = []
                folders_and_files[root_name].append((name))
            else:
                folders_and_files[root_name].append((name))

    return folders_and_files


def create_dir_name(dir_name ,path='.'):
    '''
    Keyword Arguments
    :param dir_name: the name of the directory to be created
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
            tmp_dir_name = '{0:s}_({1:2d})'.format(dir_name ,count)
            dir_name = tmp_dir_name
    pwd = "{}/{}".format(path ,dir_name)
    if pwd == "/":
        pwd = None
    return pwd


def move_to_folders(files: dict ,path='.'):
    '''
    :param files: a dictionary of directory names and the files that go into said directory
    :param path: the folder into which the folder will be created
    :return: a diction of the folders and files that were moved
    '''
    moved_files = {}
    return_val = ""
    for key in files.keys():
        moved_files[key] = []
        directory = create_dir_name(key ,path)
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
                    return_val = shutil.move(file ,directory)
                except FileNotFoundError as event_str:
                    print("Error: When create directory {} error {} was thrown\n".format(directory ,event_str))
                # expected_value = "{}/{}".format(directory, file)
    return moved_files


def parse_files_create_folder(folder_name):
    folders_and_files = collect_similar_names(folder_name)
    move_to_folders(folders_and_files)


def is_contiguious(i: int ,j: int ,distance=10):
    '''

    :param i: this is the value of the first file name enumeration
    :param j: this is the
    :param distance: the interruption between two file name, e.g. 1001, 1002, 1022, 1023

    :return: a dictionary of folder names and the files that go into the folder

    '''
    if j - i <= distance:
        return True
    else:
        return False


if __name__ == '__main__':

    files = get_command_line()
    if len(files) == 0:
        files[0] = os.getcwd()
    for file in files:
        try:
            os.chdir(file)
        except FileNotFoundError as error:
            print("There was an error" ,error)
            exit()
        pwdir = os.getcwd()
        folders_and_files = collect_similar_names(pwdir)
        if len(folders_and_files) == 1:
            updated_folders_and_files = distinguish_files(folders_and_files)
            move_to_folders(updated_folders_and_files)
        else:
            move_to_folders(folders_and_files)
