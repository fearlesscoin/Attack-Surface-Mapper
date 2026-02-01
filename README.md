##Attack Surface Mapper

## Overview
Attack Surface Mapper is a Python-based offensive security reconnaissance tool
that focuses on identifying and prioritizing exposed entry points from an
attacker’s perspective before exploitation.

Instead of directly exploiting vulnerabilities, this project models the
reconnaissance and decision-making phase used by attackers to understand where
to focus their efforts.

---

## Key Features
- Discovers reachable application endpoints
- Identifies exposed network services through basic port checks
- Classifies attack surface into High, Medium, and Low risk categories
- Supports passive reconnaissance for public websites
- Generates structured JSON output for analysis

---

## Why This Tool Matters
In real-world offensive security, attackers do not immediately exploit systems.
They first analyze the exposed attack surface to identify high-value targets.

This project demonstrates that early attacker mindset by answering:
> “Where would an attacker look first, and why?”

---

## Usage
~bash
python mapper.py -u https://example.com -H example.com --passive

---

##Output

The tool generates a structured JSON file mapping the attack surface and
categorizing entry points by risk level.

---

## Structure

mapper.py        # Main orchestrator
discover.py      # Endpoint discovery logic
ports.py         # Network exposure checks
classify.py      # Risk classification
docs/            # Project documentation
output/          # Generated attack surface output

---

#Ethical Notice

This project is for educational purposes only and must be used only on systems
you own or have explicit permission to test.


##END
