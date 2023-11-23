#!/usr/bin/python3
"""dseeeeeeee"""


class Student():
    """fdsadasdfd"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """fdasdasdadfd"""
        new_dic = {}
        if attrs is not None:
            for att in attrs:
                if att in self.__dict__.keys():
                    new_dic[att] = self.__dict__[att]
            return new_dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ssddsadsa"""
        for i in json:
            for i in self.__dict__:
                self.__dict__[i] = json[i]