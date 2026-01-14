# Linux Auth Log Analyzer (DFIR Project)

This project is a simple DFIR-focused tool to analyze Linux authentication logs
and identify suspicious login activity.

The goal of this project is to demonstrate how authentication logs can be used
during incident response to detect brute-force attempts, abnormal login behavior,
and potentially malicious IP addresses.

This is **not a SIEM** and **not a real-time tool**.  
It is a **post-incident log analysis utility**.

---

## What This Tool Does

The tool parses a Linux `auth.log` file and performs the following analysis:

- Counts failed login attempts per IP
- Detects brute-force patterns
- Identifies suspicious IP addresses using simple heuristics
- Detects time-based spikes in failed login attempts
- Generates a readable incident-style report

---

## Why Linux Auth Logs?

Linux authentication logs (`/var/log/auth.log`) are one of the first data sources
used during incident response investigations. They provide clear evidence of:

- Unauthorized access attempts
- Password guessing attacks
- Abuse of SSH and local accounts

This project focuses on **forensic analysis**, not prevention.

---

## Project Structure

linux-auth-log-analyzer/
│
├── core/
│   ├── main.py
│   └── report_generator.py
│
├── modules/
│   ├── parser.py
│   ├── failed_logins.py
│   ├── brute_force.py
│   ├── suspicious_ip.py
│   └── time_spike.py
│
├── logs/
│   └── auth.log
│
├── reports/
│   └── incident_report.txt
│
├── README.md
├── LICENSE
└── .gitignore

---

## How Detection Works (High Level)

- **Failed Logins**  
  Counts authentication failures grouped by IP address.

- **Brute-force Detection**  
  Flags IPs with a high number of failed attempts.

- **Time-Based Spike Detection**  
  Uses a sliding time window to detect abnormal bursts of failures
  that are unlikely to be caused by human behavior.

- **Suspicious IP Classification**  
  Combines multiple indicators (volume, timing, behavior) to mark IPs
  as suspicious.

---

## How to Run

From the project root directory:

## Output

The tool generates a plain text incident report that includes:

- Failed login attempts
- Possible brute-force IP addresses
- Time-based login spikes
- Suspicious IP activity

The report is saved inside the `reports/` directory.


```bash
python -m core.main



