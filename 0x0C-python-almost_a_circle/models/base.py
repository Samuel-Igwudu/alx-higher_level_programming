#!/usr/bin/python3
""" Model that contain class Base """
import json
import csv
import os.path


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
