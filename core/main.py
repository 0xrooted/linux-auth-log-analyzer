from modules.parser import parser_auth_log
from modules.failed_logins import count_failed_logins
from modules.brute_force import detect_bruteforce
from modules.suspicious_ip import detect_suspicious_ips
from modules.time_spike import detect_time_spikes
from core.report_generator import generate_incident_report

events = parser_auth_log("logs/sample_auth.log")

failed = count_failed_logins(events)
bruteforce = detect_bruteforce(events)
spikes = detect_time_spikes(events)
suspicious = detect_suspicious_ips(events, failed, bruteforce)

generate_incident_report(failed, bruteforce, spikes, suspicious)
