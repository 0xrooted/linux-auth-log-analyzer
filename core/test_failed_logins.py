import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from modules.parser import parser_auth_log
from modules.failed_logins import count_failed_logins
from modules.brute_force import detect_bruteforce
from modules.suspicious_ip import detect_suspicious_ips

events = parser_auth_log("logs/auth.log")
failed = count_failed_logins(events)
bf = detect_bruteforce(events)

result = detect_suspicious_ips(events, failed, bf)
print(result)
