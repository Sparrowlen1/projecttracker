import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.project import Project
from models.task import Task

class TestProject(unittext.TestCase):

    def setUp(self):