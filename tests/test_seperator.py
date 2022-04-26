from unittest import TestCase
import os
import tempfile
import seperator

class Test(TestCase):
    def test_split_file_name(self):
        self.assertEqual(seperator.split_file_name('Gracie-Gracie_053.jpg') == ('Gracie-Gracie' ,'_053.jpg'))
        self.assertEqual(seperator.split_file_name('Gloria Sol-GloriaSol2__cover-clean.jpg') == (
            'Gloria Sol-GloriaSol2' ,'__cover-clean.jpg'))
        self.assertEqual(seperator.split_file_name('Gloria Sol-GloriaSol2__cover.jpg') == ('Gloria Sol-GloriaSol2' ,'__cover.jpg'))

#    def test_create_dir_name(self):
#        self.fail()
