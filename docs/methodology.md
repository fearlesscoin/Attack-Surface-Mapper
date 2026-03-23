# Methodology

## Objective
The goal of this project is to understand how attackers identify and prioritize
targets during the early stages of an attack.

## Step 1: Endpoint Discovery
The tool analyzes the target application's exposed HTML to identify:
- Links
- Form actions
- Common application entry points

Optional attacker-style path guessing is supported for authorized lab
environments.

## Step 2: Exposure Identification
Basic network checks are used to identify open ports that may expose services
such as SSH or web servers.

## Step 3: Risk Classification
All discovered items are categorized based on attacker value:
- **High Risk**: Administrative interfaces, file upload points
- **Medium Risk**: Login pages, APIs, exposed services
- **Low Risk**: Static or informational resources

## Step 4: Attack Surface Mapping
The final output provides a prioritized view of the attack surface, helping
identify where an attacker would likely focus first..
