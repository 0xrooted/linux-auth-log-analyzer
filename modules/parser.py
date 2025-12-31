import re

def parse_auth_log(file_path):
    events = []

    ip_pattern = re.compile(r'from (\d+\.\d+\.\d+\.\d+)')
    user_pattern = re.compile(r'for (invalid user )?(\w+)')

    with open(file_path, "r") as file:
        for line in file:
            if "Failed password" in line:
                ip_match = ip_pattern.search(line)
                user_match = user_pattern.search(line)

                if ip_match and user_match:
                    event = {
                        "ip": ip_match.group(1),
                        "user": user_match.group(2),
                        "raw": line.strip()
                    }
                    events.append(event)

    return events
