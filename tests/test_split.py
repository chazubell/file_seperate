from unittest import TestCase
import seperator


class Test(TestCase):
    def test_split_file_name_basename(self):
        self.assertEqual(seperator.split_file_name('Gracie-Gracie_053.jpg'), ('Gracie-Gracie', '_053.jpg'))

    def test_split_file_name_cover_clean(self):
        self.assertEqual(seperator.split_file_name('Gloria Sol-GloriaSol2__cover-clean.jpg'), (
            'Gloria Sol-GloriaSol2', '__cover-clean.jpg'))

    def test_split_file_name_cover(self):
        self.assertEqual(seperator.split_file_name('Gloria Sol-GloriaSol2__cover.jpg'),
                         ('Gloria Sol-GloriaSol2', '__cover.jpg'))

#    def test_create_dir_name(self):
#        self.fail()
