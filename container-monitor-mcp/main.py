# MCP Server Implementation for Container Monitoring

import time
import psutil

class ContainerMonitor:
    def __init__(self):
        self.containers = []

    def add_container(self, container_id):
        self.containers.append(container_id)

    def monitor(self):
        while True:
            for container_id in self.containers:
                memory_info = psutil.virtual_memory()
                print(f'Container {container_id} Memory Usage: {memory_info.percent}%')
            time.sleep(5)

if __name__ == '__main__':
    monitor = ContainerMonitor()
    monitor.add_container('container_1')  # Example container ID
    monitor.monitor()