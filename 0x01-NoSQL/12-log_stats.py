#!/usr/bin/env python3

"""
getting logs
"""

from pymongo import MongoClient
if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Count documents with specific method and path
    specific_method = "GET"
    specific_path = "/status"
    specific_count = collection.count_documents(
        {"method": specific_method, "path": specific_path})
    print(f"{specific_count} status check")
