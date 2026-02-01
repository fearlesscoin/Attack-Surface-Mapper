import argparse
import json
import os

from discover import discover_endpoints
from ports import scan_ports
from classify import classify_surface


def main():
    parser = argparse.ArgumentParser(
        description="Attack Surface Mapper (Offensive Reconnaissance Tool)"
    )

    parser.add_argument(
        "-u", "--url",
        required=True,
        help="Target base URL (e.g. https://example.com)"
    )

    parser.add_argument(
        "-H", "--host",
        required=True,
        help="Target host for port checks (e.g. example.com)"
    )

    parser.add_argument(
        "--passive",
        action="store_true",
        help="Disable path guessing (safe for public websites)"
    )

    args = parser.parse_args()

    print("[*] Starting Attack Surface Mapper")
    print(f"[*] Target URL : {args.url}")
    print(f"[*] Target Host: {args.host}")

    # Step 1: Discover endpoints
    print("[*] Discovering endpoints...")
    endpoints = discover_endpoints(
        args.url,
        enable_guessing=not args.passive
    )

    # Step 2: Scan exposed ports
    print("[*] Scanning ports...")
    ports = scan_ports(args.host)

    # Step 3: Classify attack surface
    print("[*] Classifying attack surface...")
    surface = classify_surface(endpoints, ports)

    # Step 4: Save output
    os.makedirs("output", exist_ok=True)
    with open("output/surface.json", "w") as f:
        json.dump(surface, f, indent=4)

    print("[+] Attack Surface Mapping Completed")
    print(json.dumps(surface, indent=4))


if __name__ == "__main__":
    main()
