#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, fisrt_name, last_name):
        super().__init__(fisrt_name, last_name)
        self.knowledge = []
    
    def learn(self, string):
        return self.knowledge.append(string)