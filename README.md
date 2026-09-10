# SOC Project 02 — Phishing Email Investigation

## 📌 Project Overview

This project demonstrates a phishing email investigation in a controlled SOC lab environment.

The investigation covers email header analysis, IOC extraction, IP and domain investigation, DNS analysis, URL investigation, threat intelligence, and Python-based email analysis.

## 🎯 Objectives

- Analyze suspicious email headers
- Identify phishing indicators
- Extract Indicators of Compromise (IOCs)
- Investigate suspicious IP addresses and domains
- Perform DNS and URL analysis
- Use threat intelligence platforms
- Automate email analysis using Python
- Document findings in an incident investigation report

## 🛠️ Tools & Technologies

- MXToolbox
- AbuseIPDB
- DomainTools WHOIS
- URLScan
- VirusTotal
- PowerShell
- Python
- Git & GitHub

## 🔍 Investigation Findings

### Email Indicators

- Sender: `security@paypa1-alert.com`
- Reply-To: `support@paypa1-alert.com`
- Suspicious Domain: `paypa1-alert.com`
- Suspicious URL: `http://paypa1-secure-login.com/verify`
- Source IP: `45.33.32.156`

### Email Authentication

- SPF: FAIL
- DKIM: FAIL
- DMARC: FAIL

### IOC Analysis

The investigation included:

- IP reputation analysis
- Domain investigation
- WHOIS analysis
- DNS lookup
- URL analysis
- VirusTotal analysis

## 🐍 Python Automation

Two Python scripts were created:

### `email_parser.py`

Parses the `.eml` file and extracts:

- From
- To
- Subject
- Date
- Reply-To
- Received headers
- Authentication results
- Email body

### `ioc_extractor.py`

Automatically extracts:

- IPv4 addresses
- URLs
- Email addresses

## 📂 Project Structure

```text
SOC_Project_02_Phishing/
│
├── Email/
│   └── phishing_sample.eml
│
├── Investigation/
│   ├── incident_report.md
│   └── ioc_findings.md
│
├── Python/
│   ├── email_parser.py
│   └── ioc_extractor.py
│
└── Screenshot/
    ├── 01_email_header_analysis.png
    ├── 02_ip_reputation_abuseipdb.png
    ├── 03_domain_whois_analysis.png
    ├── 04_urlscan_dns_analysis.png
    ├── 05_virustotal_detection.png
    ├── 06_virustotal_vendor_analysis.png
    ├── 07_python_email_headers.png
    ├── 08_python_email_body.png
    ├── 09_dns_lookup.png
    ├── 10_python_ioc_extraction.png
    └── 11_dns_lookup_paypa1_secure_login.png
