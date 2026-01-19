# Linux Auth Log Analyzer (DFIR Project)

This project is a simple DFIR-focused tool to analyze Linux authentication logs
and identify suspicious login activity.

The goal of this project is to demonstrate how authentication logs can be used
during incident response to detect brute-force attempts, abnormal login behavior,
and potentially malicious IP addresses.

---

## What This Tool Does

The tool parses a Linux `auth.log` file and performs the following analysis:

- Counts failed login attempts per IP
- Detects brute-force patterns
- Identifies suspicious IP addresses using simple heuristics
- Detects time-based spikes in failed login attempts
- Generates a readable incident-style report

The idea is to simulate how a SOC analyst or DFIR analyst might triage authentication logs during an investigation.
---

## Why Linux Auth Logs?

Linux authentication logs (`/var/log/auth.log`) are one of the first data sources
used during incident response investigations. They provide clear evidence of:

- Unauthorized access attempts
- Password guessing and brute_force attacks
- Abuse of SSH and local accounts
- Repeated login faliurs from external IPs

This project focuses on **forensic analysis**, not prevention.

---

## Project Structure
```
linux-auth-log-analyzer/
│
├── core/
│   └── main.py
│
├── modules/
│   ├── parser.py
│   ├── failed_logins.py
│   ├── brute_force.py
│   ├── time_spike.py
│   ├── suspicious_ip.py
│   ├── evidence_exporter.py
│   └── report_generator.py
│
├── logs/
│   └── sample_auth.log
│
├── evidence_data/
│   ├── failed_attempts.csv
│   ├── bruteforce_ips.csv
│   ├── time_spike_events.csv
│   └── suspicious_ips.csv
│
├── reports/
│   └── incident_report.txt
│
├── LICENSE
└── README.md
```
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

## Output

The tool generates a plain text incident report that includes:

- Failed login attempts
- Possible brute-force IP addresses
- Time-based login spikes
- Suspicious IP activity
- CSV files containing extracted evidence (failed attempts, brute-force IPs, time spikes, suspicious IPs)

All outputs are stored in the evidence_data/ and reports/ directories.

## Note

The `sample_auth.log` file included in this repository is **synthetically generated** for learning and demonstration purposes only.

It does **not** belong to any real system, server, or organization.  
All IP addresses, usernames, and timestamps are dummy and used only to simulate real-world DFIR scenarios such as brute-force attacks and suspicious login behavior.

## How to Run

From the project root directory:

```bash
python -m core.main
