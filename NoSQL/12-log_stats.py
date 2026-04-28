cat <<EOF > 12-log_stats.py
#!/usr/bin/env python3
""" Script que proporciona estadísticas sobre logs de Nginx """
from pymongo import MongoClient

def log_stats():
    """ Conecta a MongoDB y extrae estadísticas """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
EOF
