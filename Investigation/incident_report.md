# Phishing Email Investigation Report

## Ticket

INC-2026-002

## Analyst

Yogesh A

## Date

2026-06-28

## 1. Incident Summary

A suspicious phishing email was identified and investigated in a controlled SOC lab environment.

The email used a lookalike domain, suspicious URL, failed email authentication checks, and a source IP with abuse reports.

## 2. Email Details

- Sender: security@paypa1-alert.com
- Reply-To: support@paypa1-alert.com
- Subject: URGENT: Your account has been suspended
- Source IP: 45.33.32.156
- Suspicious Domain: paypa1-alert.com
- Suspicious URL: http://paypa1-secure-login.com/verify

## 3. Email Authentication Analysis

- SPF: FAIL
- DKIM: FAIL
- DMARC: FAIL

The failed authentication results are suspicious and require further investigation.

## 4. IP Investigation

### AbuseIPDB

- IP: 45.33.32.156
- Abuse Reports: 22
- Abuse Confidence: 14%
- ISP: Linode
- Usage Type: Data Center/Web Hosting/Transit
- Country: United States
- ASN: AS63949

The IP has abuse reports, but the 14% abuse confidence score alone does not confirm malicious activity.

## 5. Domain Investigation

### DomainTools

- Domain: paypa1-alert.com
- Status: Never Registered Before
- WHOIS: Not Available

The domain uses a lookalike technique (`paypa1` instead of `paypal`), which is a phishing indicator.

## 6. URL Investigation

### URLScan

- URL: http://paypa1-secure-login.com/verify
- Result: DNS Error
- Domain could not be resolved

### DNS Lookup

- `paypa1-alert.com` → DNS name does not exist
- `paypa1-secure-login.com` → DNS name does not exist

## 7. VirusTotal Analysis

The suspicious URL was analyzed using VirusTotal.

- Displayed security vendor results were Clean.
- No malicious detection was shown in the captured results.

A clean VirusTotal result does not by itself prove that the URL is safe.

## 8. Indicators of Compromise (IOCs)

### Email Addresses

- security@paypa1-alert.com
- support@paypa1-alert.com
- employee@company.com

### IP Address

- 45.33.32.156

### Domains

- paypa1-alert.com
- paypa1-secure-login.com

### URL

- http://paypa1-secure-login.com/verify

## MITRE ATT&CK Mapping

- T1566.001: Spearphishing Attachment
- T1598.003: Phishing for Information

## 9. Severity

**Medium**

## 10. Final Assessment

The email contains multiple phishing indicators, including:

- Lookalike domain
- Suspicious URL
- SPF, DKIM, and DMARC failures
- IP address with abuse reports
- DNS resolution failure

Based on the available evidence, the email should be treated as a suspicious phishing attempt.

Further correlation with SIEM logs and endpoint activity is recommended before making a final verdict.

## 11. Recommended SOC Actions

1. Quarantine the suspicious email.
2. Search SIEM logs for the identified IOCs.
3. Monitor activity related to the source IP.
4. Check whether the URL was accessed by any users.
5. Check for credential submission or account compromise.
6. Block the indicators if malicious activity is confirmed.
7. Preserve the email and investigation evidence.
8. Reset affected credentials if compromise is confirmed.