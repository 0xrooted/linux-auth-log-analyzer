from modules.parser import parser_auth_log
from modules.failed_logins import count_failed_logins

events = parser_auth_log("logs/auth.log")
result = count_failed_logins(events)
print(result)
