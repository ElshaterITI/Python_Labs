import re

def extract_emails():
    data = open("access.log", "r")
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+"

    emails = re.findall(pattern, data.read())

    unique_emails = sorted(set(emails))

    file = open("valid_emails.txt", "w")
    file.write("\n".join(unique_emails))

    print(f"Found {len(unique_emails)} unique valid emails.")
    print("Emails saved in valid_emails.txt")
    data.close()
    file.close()
