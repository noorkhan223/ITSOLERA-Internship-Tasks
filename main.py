import argparse
import logging
import datetime
import os

from modules import whois_lookup, dns_enum, subdomain_enum, port_scan, banner_grab, tech_detect

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def save_report(domain, data):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{domain}_report_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(data)
    print(f"\n[+] Report saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Custom Recon Tool")
    parser.add_argument("domain", help="Target domain")
    parser.add_argument("--whois", action="store_true")
    parser.add_argument("--dns", action="store_true")
    parser.add_argument("--subdomains", action="store_true")
    parser.add_argument("--portscan", action="store_true")
    parser.add_argument("--banner", action="store_true")
    parser.add_argument("--tech", action="store_true")
    
    args = parser.parse_args()
    domain = args.domain
    report = f"Recon Report for {domain}\nGenerated: {datetime.datetime.now()}\n\n"

    if args.whois:
        logging.info("Running WHOIS lookup...")
        report += "\n--- WHOIS ---\n" + whois_lookup.perform_whois(domain) + "\n"

    if args.dns:
        logging.info("Running DNS Enumeration...")
        dns_results = dns_enum.dns_lookup(domain)
        for rtype, records in dns_results.items():
            report += f"\n{rtype} Records:\n" + "\n".join(records) + "\n"

    if args.subdomains:
        logging.info("Running Subdomain Enumeration...")
        subs = subdomain_enum.subdomains_crtsh(domain)
        report += "\n--- Subdomains ---\n" + "\n".join(subs) + "\n"

    if args.portscan:
        logging.info("Running Port Scan...")
        open_ports = port_scan.scan_ports(domain)
        report += "\n--- Open Ports ---\n" + ", ".join(map(str, open_ports)) + "\n"

    if args.banner:
        logging.info("Running Banner Grabbing...")
        for port in [80, 443]:
            banner = banner_grab.grab_banner(domain, port)
            report += f"\nBanner on port {port}: {banner}\n"

    if args.tech:
        logging.info("Detecting Technologies...")
        tech = tech_detect.detect_tech(domain)
        for k, v in tech.items():
            report += f"{k}: {v}\n"

    save_report(domain, report)

if __name__ == "__main__":
    main()
