'''psutil (python system and process utilities) is a cross-platform
library for retrieving information on running processes and 
system utilization (CPU, memory, disks, network, sensors) in Python.
'''

import psutil
import platform

# Get machine-info
machine_info = platform.uname()
print(machine_info)

# number of cpu
print(psutil.cpu_count())

# memory info
print(psutil.virtual_memory())

# User count
print(psutil.users())

# Check boot time (seconds)
print(psutil.boot_time())

# Disk partitions and usage info
print(psutil.disk_partitions())

# Network info
print(psutil.net_if_addrs())
