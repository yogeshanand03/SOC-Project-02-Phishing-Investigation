\# Phishing Email IOC Findings



\## Email Indicators



\- Sender: security@paypa1-alert.com

\- Reply-To: support@paypa1-alert.com

\- Suspicious Domain: paypa1-alert.com

\- Suspicious URL: http://paypa1-secure-login.com/verify

\- Source IP: 45.33.32.156



\## Authentication Findings



\- SPF: FAIL

\- DKIM: FAIL

\- DMARC: FAIL



\## External Investigation



\### AbuseIPDB

\- IP: 45.33.32.156

\- Abuse Reports: 22

\- Abuse Confidence: 14%

\- ISP: Linode

\- Usage Type: Data Center/Web Hosting/Transit



\### DomainTools

\- Domain: paypa1-alert.com

\- Status: Never Registered Before

\- WHOIS: Not Available



\### URLScan

\- URL: http://paypa1-secure-login.com/verify

\- Result: DNS Error

\- Domain could not be resolved



\### VirusTotal

\- URL analyzed successfully

\- Displayed security vendor results were Clean

\- No malicious detection was shown in the captured results



\## Initial Assessment



The email contains multiple phishing indicators including a

lookalike domain, suspicious URL, failed email authentication

checks, and a hosting IP with abuse reports.



The evidence should be correlated before making a final verdict.

