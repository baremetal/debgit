import os
import unittest

from debgit import reprepro

SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_DIR = SCRIPT_DIR if SCRIPT_DIR != '' else '.'

TEMPLATE = os.path.join(SCRIPT_DIR, 'files', 'reprepro_template.txt')

class RepreproTestCase(unittest.TestCase):
    def test_get_section(self):
        section = reprepro.Section(TEMPLATE)
        output = section.render('hello')

        self.assertTrue('Codename: hello' in output)
        self.assertTrue('Description: AppScale Systems package repository for "hello" code branch.' in output)
