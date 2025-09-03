import requests
import threading
import time

def send_request():
    try:
        res = requests.get("http://p2p-node-service.p2p-benchmark.svc.cluster.local")
        print(f"Status: {res.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        threads = []
        for _ in range(20):
            t = threading.Thread(target=send_request)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        time.sleep(1)
