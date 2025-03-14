import os
import subprocess
import logging

# Configure logging
logging.basicConfig(filename="network_diagnostics.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def check_ip_conflicts():
    """Check for IP conflicts using ARP table"""
    print("\n[+] Checking for IP conflicts...")
    result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    logging.info("IP Conflict Check:\n" + result.stdout)
    print(result.stdout)

def check_dns_resolution(domain):
    """Check DNS resolution for a given domain"""
    print(f"\n[+] Checking DNS resolution for {domain}...")
    result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
    logging.info(f"DNS Resolution for {domain}:\n" + result.stdout)
    print(result.stdout)

def check_dhcp_leases():
    """Check assigned DHCP leases"""
    print("\n[+] Checking DHCP lease allocations...")
    lease_file = "/var/lib/dhcp/dhcpd.leases"
    if os.path.exists(lease_file):
        with open(lease_file, "r") as file:
            lease_data = file.read()
            logging.info("DHCP Lease File Content:\n" + lease_data)
            print(lease_data)
    else:
        logging.warning("DHCP lease file not found.")
        print("[-] DHCP lease file not found.")

def generate_network_report():
    """Generate a summary network report"""
    print("\n[+] Generating Network Diagnostic Report...")
    report = "=== NETWORK DIAGNOSTIC REPORT ===\n"
    
    # Capture current network configuration
    result = subprocess.run(["ip", "a"], capture_output=True, text=True)
    report += "\n[Network Interfaces]\n" + result.stdout

    # Capture routing table
    result = subprocess.run(["ip", "route"], capture_output=True, text=True)
    report += "\n[Routing Table]\n" + result.stdout

    # Capture DNS settings
    result = subprocess.run(["cat", "/etc/resolv.conf"], capture_output=True, text=True)
    report += "\n[DNS Configuration]\n" + result.stdout

    # Save report
    with open("network_report.txt", "w") as file:
        file.write(report)
    logging.info("Network Diagnostic Report generated.")

    print("[+] Report saved as 'network_report.txt'")

# Run troubleshooting checks
check_ip_conflicts()
check_dns_resolution("example.local")
check_dns_resolution("google.com")
check_dhcp_leases()
generate_network_report()
