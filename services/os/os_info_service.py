# -*- coding: utf-8 -*-
import ipaddress
import os
import platform
import re
import socket
import threading
import uuid
from datetime import datetime
from time import sleep

import cpuinfo
import psutil


class OsInfoService:
    max_threads = 50
    final = {}
    port = 80

    def get_size(self, bytes, suffix='B'):
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor

    def get_sys_info(self) -> None:
        print("=" * 40, "System information", "=" * 40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")
        print(f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}")
        print(f"Ip-Address: {socket.gethostbyname(socket.gethostname())}")
        print(f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")

    def get_boot_time(self) -> None:
        # Boot Time
        print("=" * 40, "Boot Time", "=" * 40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    def get_cpuinfo(self) -> None:
        # print CPU information
        print("=" * 40, "CPU Info", "=" * 40)

        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))

        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

        # CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    def get_memroy_info(self) -> None:
        # Memory Information
        print("=" * 40, "Memory Information", "=" * 40)
        svmem = psutil.virtual_memory()
        print(f"Total: {self.get_size(svmem.total)}")
        print(f"Available: {self.get_size(svmem.available)}")
        print(f"Used: {self.get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")

        print("=" * 40, "SWAP", "=" * 40)
        swap = psutil.swap_memory()
        print(f"Total: {self.get_size(swap.total)}")
        print(f"Free: {self.get_size(swap.free)}")
        print(f"Used: {self.get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")

    def get_disk_info(self) -> None:
        # Disk Information
        print("=" * 40, "Disk Information", "=" * 40)
        print("Partitions and Usage:")

        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {self.get_size(partition_usage.total)}")
            print(f"  Used: {self.get_size(partition_usage.used)}")
            print(f"  Free: {self.get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")

        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {self.get_size(disk_io.read_bytes)}")
        print(f"Total write: {self.get_size(disk_io.write_bytes)}")

    def get_network_info(self) -> None:
        # Network information
        print("=" * 40, "Network Information", "=" * 40)

        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {self.get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {self.get_size(net_io.bytes_recv)}")

    def get_port_open(self) -> None:
        for ip in ipaddress.IPv4Network('10.66.50.39/24'):
            threading.Thread(target=self.check_port, args=[str(ip), self.port]).start()
            # limit the number of threads.
            while threading.active_count() > self.max_threads:
                sleep(1)

        print(self.final)

    def check_port(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
            # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
            socket.setdefaulttimeout(2.0)  # seconds (float)
            result = sock.connect_ex((ip, port))
            if result == 0:
                # print ("Port is open")
                self.final[ip] = "OPEN"
            else:
                # print ("Port is closed/filtered")
                # self.final[ip] = "CLOSED"
                pass
            sock.close()
        except:
            pass

    def get_user_info(self):
        print("=" * 40, "User Information", "=" * 40)
        print(f'user {os.getlogin()}')

    def system_info(self):
        self.get_user_info()
        self.get_sys_info()
        self.get_boot_time()
        self.get_cpuinfo()
        self.get_memroy_info()
        self.get_disk_info()
        self.get_network_info()
        # self.get_port_open()


if __name__ == '__main__':
    OsInfoService().system_info()
