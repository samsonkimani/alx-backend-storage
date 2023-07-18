#!/usr/bin/env python3

"""
writting a function to get all documents
"""


def list_all(mongo_collection):
    """ list all function """
    return mongo_collection.find()
