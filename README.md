# DHCP Server Setup and Network Configuration

## Overview

This project involves the configuration and management of a **DHCP server** for a local network, enabling the efficient allocation of dynamic IP addresses to devices within the network. The setup ensures that all networked devices receive valid IP addresses, DNS configuration is properly handled, and there is no conflict or error in IP address distribution. Additionally, troubleshooting tools have been developed to analyze and resolve network connectivity issues, particularly those related to IP configuration and DNS resolution.

## Table of Contents
1. [Introduction](#introduction)
2. [DHCP Server Setup](#dhcp-server-setup)
3. [DNS Server Configuration](#dns-server-configuration)
4. [Monitoring IP Address Distribution](#monitoring-ip-address-distribution)
5. [Network Troubleshooting Tools](#network-troubleshooting-tools)
6. [Conclusion](#conclusion)

---

## 1. Introduction

A **Dynamic Host Configuration Protocol (DHCP) server** is an essential network component that automatically assigns IP addresses to devices on a local network. The key objective of this project was to set up a DHCP server that provides **dynamic IP address allocation** and integrates **DNS services** for efficient network name resolution. Additionally, network monitoring and troubleshooting tools were created to ensure smooth network operation.

## 2. DHCP Server Setup

### Objective:
- Configure a DHCP server to automatically allocate IP addresses to devices on a local network.

### Steps:
1. **Install the DHCP Server:**
   - On a Linux-based server, install the DHCP server using the following command:
     ```bash
     sudo apt-get install isc-dhcp-server
     ```
2. **Configure DHCP Server:**
   - Edit the configuration file (`/etc/dhcp/dhcpd.conf`) to define the DHCP scope, which specifies the range of IP addresses to be allocated to devices:
     ```bash
     subnet 192.168.1.0 netmask 255.255.255.0 {
         range 192.168.*.* 192.168.*.*;
         option domain-name-servers 8.8.8.8, 8.8.4.4;
         option routers 192.168.1.1;
         option subnet-mask 255.255.255.0;
         default-lease-time 600;
         max-lease-time 7200;
     }
     ```
3. **Start and Enable the DHCP Service:**
   - Enable and start the DHCP server service to make sure it runs after boot:
     ```bash
     sudo systemctl enable isc-dhcp-server
     sudo systemctl start isc-dhcp-server
     ```

4. **Verify DHCP Server Functionality:**
   - Test the DHCP server by connecting a device to the network. The device should automatically receive an IP address within the specified range.

## 3. DNS Server Configuration

### Objective:
- Integrate **DNS servers** into the DHCP configuration to ensure smooth **network name resolution**.

### Steps:
1. **Configure DNS Servers in the DHCP Settings:**
   - In the DHCP configuration file (`/etc/dhcp/dhcpd.conf`), the `option domain-name-servers` directive defines the DNS servers used by client devices:
     ```bash
     option domain-name-servers 8.8.8.8, 8.8.4.4;
     ```

2. **Test DNS Resolution:**
   - After configuring DNS servers, verify the setup by pinging domain names (e.g., `ping google.com`) from a client device. The device should resolve domain names correctly.

## 4. Monitoring IP Address Distribution

### Objective:
- Continuously monitor the IP address distribution to ensure no conflicts or errors occur.

### Steps:
1. **View DHCP Leases:**
   - Monitor the IP addresses that have been assigned by the DHCP server by checking the lease file:
     ```bash
     cat /var/lib/dhcp/dhcpd.leases
     ```

2. **Configure IP Conflict Detection:**
   - The DHCP server can detect IP conflicts and ensure that no duplicate IP addresses are assigned. This is typically done by setting the `ping-check` option in the server configuration to verify IP addresses before allocation.

3. **Check DHCP Server Logs:**
   - Review DHCP logs to ensure that there are no errors or issues with IP allocation:
     ```bash
     cat /var/log/syslog | grep dhclient
     ```

4. **Monitor DHCP Server Performance:**
   - Use tools like `netstat` and `iftop` to monitor network traffic and DHCP server performance in real-time.

## 5. Network Troubleshooting Tools

### Objective:
- Develop and implement **network troubleshooting tools** to diagnose and resolve common network configuration issues.

### Tools Developed:
1. **IP Configuration Troubleshooting Script:**
   - A Python script that automates the process of verifying the correct configuration of network interfaces, IP addresses, and routes.
     ```python
     import os
     import subprocess

     def check_ip_configuration():
         result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
         print(result.stdout.decode('utf-8'))

     def check_default_gateway():
         result = subprocess.run(['ip route'], stdout=subprocess.PIPE)
         print(result.stdout.decode('utf-8'))

     if __name__ == "__main__":
         check_ip_configuration()
         check_default_gateway()
     ```

2. **DNS Resolution Troubleshooting Script:**
   - A Python script that tests DNS resolution by querying various domain names.
     ```python
     import socket

     def test_dns_resolution(domain):
         try:
             ip_address = socket.gethostbyname(domain)
             print(f"Domain {domain} resolved to {ip_address}")
         except socket.gaierror:
             print(f"DNS resolution failed for {domain}")

     if __name__ == "__main__":
         domains = ["google.com", "yahoo.com", "example.com"]
         for domain in domains:
             test_dns_resolution(domain)
     ```

3. **Ping Test:**
   - A simple script to ping network devices and verify their reachability.
     ```bash
     ping -c 4 192.168.1.1  # Ping the router
     ```

4. **Network Connectivity Check:**
   - Use `ping` and `traceroute` to diagnose connectivity issues between network devices and external servers.

## 6. Conclusion

The successful implementation of the **DHCP server** and **DNS configuration** has streamlined IP address allocation and ensured seamless network communication within the local network. Additionally, the developed troubleshooting tools assist in diagnosing and resolving network-related issues efficiently. Regular monitoring and proactive maintenance of the DHCP server ensure that IP conflicts and configuration errors are minimized, ensuring smooth network operations.

For additional resources, troubleshooting tips, or to contribute to this repository, feel free to open an issue or submit a pull request.

---

**License:** [MIT License](https://opensource.org/licenses/MIT)

