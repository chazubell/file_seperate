from unittest import TestCase
import seperator
import os
import tempfile
base_folder_name = "/Volumes/One Touch/2022-04-12/Earmiller/femjoy_Aida"
base_file_name = "femjoy_Ellen - Bedtime Story"
sample_dir = 'data'

class Test(TestCase):
    def test_create_dir(self):
        test_dirname = base_file_name
        with tempfile.TemporaryDirectory() as tempdirname:
            os.chdir(tempdirname)
            expected_dir_name = "{}/{}".format(tempdirname, test_dirname)
            resultant_dir_name = seperator.create_dir_name(test_dirname, tempdirname)
            self.assertEqual(expected_dir_name,resultant_dir_name)

    def test_move_to_folders(self):
        keys = seperator.collect_similar_names(base_folder_name)
        with tempfile.TemporaryDirectory() as tempdirname:
            for file in keys[base_file_name]:
                seperator.move_to_folders()
        '''How to sample the values?'''


