# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 07:47:45 2022

@author: E461183
"""

# content of test_file_seperate.py
import os
import tempfile

import seperator



def test_split_file_name():
    assert seperator.split_file_name('Gracie-Gracie_053.jpg') == ('Gracie-Gracie', '_053.jpg')
    assert seperator.split_file_name('Gloria Sol-GloriaSol2__cover-clean.jpg') == (
    'Gloria Sol-GloriaSol2', '__cover-clean.jpg')
    assert seperator.split_file_name('Gloria Sol-GloriaSol2__cover.jpg') == ('Gloria Sol-GloriaSol2', '__cover.jpg')


def test_collect_similar_names():
    keys = seperator.collect_similar_names('foo.txt')
    assert keys.get('Gracie-Gracie') == ['Gracie-Gracie_001.jpg\n' ,'Gracie-Gracie_002.jpg\n' ,
                                         'Gracie-Gracie_003.jpg\n' ,'Gracie-Gracie_004.jpg\n' ,
                                         'Gracie-Gracie_005.jpg\n' ,'Gracie-Gracie_006.jpg\n' ,
                                         'Gracie-Gracie_007.jpg\n' ,'Gracie-Gracie_008.jpg\n' ,
                                         'Gracie-Gracie_009.jpg\n' ,'Gracie-Gracie_010.jpg\n' ,
                                         'Gracie-Gracie_011.jpg\n' ,'Gracie-Gracie_012.jpg\n' ,
                                         'Gracie-Gracie_026.jpg\n' ,'Gracie-Gracie_027.jpg\n' ,
                                         'Gracie-Gracie_028.jpg\n' ,'Gracie-Gracie_029.jpg\n' ,
                                         'Gracie-Gracie_030.jpg\n' ,'Gracie-Gracie_031.jpg\n' ,
                                         'Gracie-Gracie_032.jpg\n' ,'Gracie-Gracie_033.jpg\n' ,
                                         'Gracie-Gracie_034.jpg\n' ,'Gracie-Gracie_035.jpg\n' ,
                                         'Gracie-Gracie_036.jpg\n' ,'Gracie-Gracie_037.jpg\n' ,
                                         'Gracie-Gracie_038.jpg\n' ,'Gracie-Gracie_039.jpg\n' ,
                                         'Gracie-Gracie_040.jpg\n' ,'Gracie-Gracie_041.jpg\n' ,
                                         'Gracie-Gracie_042.jpg\n' ,'Gracie-Gracie_043.jpg\n' ,
                                         'Gracie-Gracie_044.jpg' ,'Gracie-Gracie_045.jpg\n' ,
                                         'Gracie-Gracie_046.jpg\n' ,'Gracie-Gracie_047.jpg\n' ,
                                         'Gracie-Gracie_048.jpg\n' ,'Gracie-Gracie_049.jpg\n' ,
                                         'Gracie-Gracie_050.jpg\n' ,'Gracie-Gracie_051.jpg\n' ,
                                         'Gracie-Gracie_052.jpg\n' ,'Gracie-Gracie_053.jpg\n' ,
                                         'Gracie-Gracie_054.jpg\n' ,'Gracie-Gracie_055.jpg\n' ,
                                         'Gracie-Gracie_056.jpg\n' ,'Gracie-Gracie_057.jpg\n' ,
                                         'Gracie-Gracie_058.jpg\n' ,'Gracie-Gracie_059.jpg\n' ,
                                         'Gracie-Gracie_060.jpg\n' ,'Gracie-Gracie_061.jpg\n' ,
                                         'Gracie-Gracie_062.jpg\n' ,'Gracie-Gracie_063.jpg\n' ,
                                         'Gracie-Gracie_064.jpg\n' ,'Gracie-Gracie__cover-clean.jpg\n' ,
                                         'Gracie-Gracie__cover.jpg\n']
    assert keys.get('foo.txt') == None
    keys = seperator.collect_similar_names("/Volumes/One Touch/2022-04-12/Earmiller/femjoy_Aida")
    assert keys.get('femjoy_Ellen - Bedtime Story') != (
    'femjoy_Ellen - Bedtime Story_000.jpg' , 'femjoy_Ellen - Bedtime Story_001.jpg' ,
    'femjoy_Ellen - Bedtime Story_002.jpg' , 'femjoy_Ellen - Bedtime Story_003.jpg' ,
    'femjoy_Ellen - Bedtime Story_004.jpg' , 'femjoy_Ellen - Bedtime Story_005.jpg' ,
    'femjoy_Ellen - Bedtime Story_006.jpg' , 'femjoy_Ellen - Bedtime Story_007.jpg' ,
    'femjoy_Ellen - Bedtime Story_008.jpg' , 'femjoy_Ellen - Bedtime Story_009.jpg' ,
    'femjoy_Ellen - Bedtime Story_010.jpg' , 'femjoy_Ellen - Bedtime Story_011.jpg' ,
    'femjoy_Ellen - Bedtime Story_012.jpg' , 'femjoy_Ellen - Bedtime Story_013.jpg' ,
    'femjoy_Ellen - Bedtime Story_014.jpg' , 'femjoy_Ellen - Bedtime Story_015.jpg' ,
    'femjoy_Ellen - Bedtime Story_016.jpg' , 'femjoy_Ellen - Bedtime Story_017.jpg' ,
    'femjoy_Ellen - Bedtime Story_018.jpg' , 'femjoy_Ellen - Bedtime Story_019.jpg' ,
    'femjoy_Ellen - Bedtime Story_020.jpg' , 'femjoy_Ellen - Bedtime Story_021.jpg' ,
    'femjoy_Ellen - Bedtime Story_022.jpg' , 'femjoy_Ellen - Bedtime Story_023.jpg' ,
    'femjoy_Ellen - Bedtime Story_024.jpg' , 'femjoy_Ellen - Bedtime Story_025.jpg' ,
    'femjoy_Ellen - Bedtime Story_026.jpg' , 'femjoy_Ellen - Bedtime Story_027.jpg' ,
    'femjoy_Ellen - Bedtime Story_028.jpg' , 'femjoy_Ellen - Bedtime Story_029.jpg' ,
    'femjoy_Ellen - Bedtime Story_030.jpg' , 'femjoy_Ellen - Bedtime Story_031.jpg' ,
    'femjoy_Ellen - Bedtime Story_032.jpg' , 'femjoy_Ellen - Bedtime Story_033.jpg' ,
    'femjoy_Ellen - Bedtime Story_034.jpg' , 'femjoy_Ellen - Bedtime Story_035.jpg' ,
    'femjoy_Ellen - Bedtime Story_036.jpg' , 'femjoy_Ellen - Bedtime Story_037.jpg' ,
    'femjoy_Ellen - Bedtime Story_038.jpg' , 'femjoy_Ellen - Bedtime Story_039.jpg' ,
    'femjoy_Ellen - Bedtime Story_040.jpg' , 'femjoy_Ellen - Bedtime Story_041.jpg' ,
    'femjoy_Ellen - Bedtime Story_042.jpg' , 'femjoy_Ellen - Bedtime Story_043.jpg' ,
    'femjoy_Ellen - Bedtime Story_044.jpg' , 'femjoy_Ellen - Bedtime Story_045.jpg' ,
    'femjoy_Ellen - Bedtime Story_046.jpg' , 'femjoy_Ellen - Bedtime Story_047.jpg' ,
    'femjoy_Ellen - Bedtime Story_048.jpg' , 'femjoy_Ellen - Bedtime Story_049.jpg' ,
    'femjoy_Ellen - Bedtime Story_050.jpg' , 'femjoy_Ellen - Bedtime Story_051.jpg' ,
    'femjoy_Ellen - Bedtime Story_052.jpg' , 'femjoy_Ellen - Bedtime Story_053.jpg' ,
    'femjoy_Ellen - Bedtime Story_054.jpg' , 'femjoy_Ellen - Bedtime Story_055.jpg' ,
    'femjoy_Ellen - Bedtime Story_056.jpg' , 'femjoy_Ellen - Bedtime Story_057.jpg' ,
    'femjoy_Ellen - Bedtime Story_058.jpg' , 'femjoy_Ellen - Bedtime Story_059.jpg')


def test_create_dir():
    with tempfile.TemporaryDirectory() as tempdirname:
        os.chdir(tempdirname)
        seperator.create_dir_name('femjoy_Ellen - Bedtime Story') == tempdirname + '/' + 'femjoy_Ellen - Bedtime Story'

def test_move_to_folders():
    keys = seperator.collect_similar_names("/Volumes/One Touch/2022-04-12/Earmiller/femjoy_Aida")

