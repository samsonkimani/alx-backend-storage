#!/usr/bin/env python3

"""
improving the log stats
"""
from pymongo import MongoClient


def log_stats():
    """ log stats """
    client = MongoClient('mongodb://localhost:27017')

    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in top_ips:
        ip_address = ip["_id"]
        count = ip["count"]
        print(f"    {ip_address}: {count}")


if __name__ == "__main__":
    log_stats()
