# Architecture

## Overview
The Attack Surface Mapper is designed to simulate the reconnaissance phase of an
offensive security assessment. Instead of exploiting vulnerabilities, the tool
focuses on identifying and organizing exposed entry points that an attacker
would analyze before launching an attack.

## High-Level Flow
1. The user provides a target URL and host.
2. The system discovers reachable application endpoints.
3. The system checks for exposed network services.
4. All discovered entries are classified based on attacker interest.
5. The results are stored in a structured JSON format.

## Components
- **discover.py**  
  Responsible for endpoint discovery using HTML parsing and optional
  attacker-style path guessing.

- **ports.py**  
  Performs basic network port checks to identify exposed services.

- **classify.py**  
  Assigns risk levels (High, Medium, Low) to discovered entries.

- **mapper.py**  
  Orchestrates the complete workflow and generates the final output.

## Design Philosophy
The architecture prioritizes clarity, modularity, and attacker mindset over
complex automation or exploitation.

