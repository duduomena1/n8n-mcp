# Container Service

This module provides operations for managing Docker containers, including starting, stopping, and monitoring containers.

## Functions

- `start_container(container_name: str)`: Starts a Docker container by name.
- `stop_container(container_name: str)`: Stops a Docker container by name.
- `monitor_container(container_name: str)`: Monitors the status of a Docker container.

## Example Usage

```python
if __name__ == '__main__':
    start_container('my_container')
    stop_container('my_container')
    monitor_container('my_container')
```