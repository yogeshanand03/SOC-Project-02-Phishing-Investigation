import re

# Read phishing email
email_file = "../Email/phishing_sample.eml"

with open(email_file, "r", encoding="utf-8") as f:
    content = f.read()

print("===== IOC EXTRACTION =====")

# Extract IPv4 addresses
ips = sorted(set(re.findall(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    content
)))

# Extract URLs
urls = sorted(set(re.findall(
    r"https?://[^\s\"<>]+",
    content
)))

# Extract email addresses
emails = sorted(set(re.findall(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    content
)))

print("\n[+] IP Addresses:")
print("\n".join(ips))

print("\n[+] URLs:")
print("\n".join(urls))

print("\n[+] Email Addresses:")
print("\n".join(emails))