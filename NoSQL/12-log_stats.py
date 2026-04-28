#!/usr/bin/env python3
""" Script que proporciona estadísticas sobre logs de Nginx en MongoDB """
from pymongo import MongoClient


def log_stats():
    """ Conecta a MongoDB y extrae estadísticas de la colección nginx """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Conteo total de logs
    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")

    # Estadísticas por métodos
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Conteo específico de GET y path /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
