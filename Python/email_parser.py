from email import policy
from email.parser import BytesParser

email_file = "../Email/phishing_sample.eml"

with open(email_file, "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

print("===== PHISHING EMAIL ANALYSIS =====")

print("\n[+] From:")
print(msg["From"])

print("\n[+] To:")
print(msg["To"])

print("\n[+] Subject:")
print(msg["Subject"])

print("\n[+] Date:")
print(msg["Date"])

print("\n[+] Reply-To:")
print(msg["Reply-To"])

print("\n[+] Received:")
print(msg["Received"])

print("\n[+] Authentication Results:")
print(msg["Authentication-Results"])

print("\n===== EMAIL BODY =====")

if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            print(part.get_content())
            break
else:
    print(msg.get_content())