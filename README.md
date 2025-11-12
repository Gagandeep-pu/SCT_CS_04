Educational Keystroke Logger — Lab / Defensive Demo
Important — read before using: This repository contains a simple keystroke-capture proof-of-concept intended only for defensive research, security education, or testing on machines you own or where you have explicit, documented consent to operate. Do not deploy this on other people’s systems or on production devices. Unauthorized use is illegal and unethical.
Purpose
This repository demonstrates how low-level keyboard event capture can be implemented for educational and defensive purposes:
Teaching how keystroke-capture works so defenders can better detect and remediate such tools.
Building lab exercises to show the impact of endpoint telemetry and why endpoint protections matter.
Testing detection rules in a controlled environment.
NOT intended for malicious use. The repository deliberately omits any instructions for stealthy deployment, exfiltration, or misuse.
What’s included
keylogger.py — minimal example that records key events (timestamps + key) to a local file.
Example screenshots (from a controlled lab): /screenshots/ showing the script, captured logs, and test pages.
key_log.txt — an example output (sanitized) to demonstrate what logged data looks like.
README.md — this document.
Legal & Ethical Notice
You must obey local laws and organizational policies.
Only run this code on systems you own or where you have explicit written permission.
Use this code only in isolated lab environments (virtual machines or air-gapped testbeds).
The repository owner and contributors are not responsible for misuse.
If you are unsure, stop and seek authorization from the relevant owner or legal counsel.
Safe Lab Setup (recommended)
Create an isolated virtual machine (VM) with a snapshot/backup.
Do not connect the VM to sensitive networks (use an isolated network or host-only adapter).
Use test accounts and dummy credentials for any interaction with websites.
Revert the VM snapshot after testing and securely delete logs.
How to run (defensive / lab use only)
Reminder: Only on machines with explicit permission.
Install required dependencies (example uses pynput):
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
requirements.txt:
pynput
Run in a terminal:
python keylogger.py
Stop the script with Ctrl+C (or the appropriate interruption method), then inspect the key_log.txt file for output.
Example output (sanitized)
2025-11-11 09:25:01: f
2025-11-11 09:25:02: a
2025-11-11 09:25:03: c
2025-11-11 09:25:10: [Key.shift]
2025-11-11 09:25:20: [Key.backspace]
...
Defensive/Detection Guidance
If you are building defensive controls, consider:
Monitoring for unexpected processes that read input devices or call low-level input APIs.
File monitoring for creation of unusual log files in user directories.
Endpoint detection rules for processes using keyboard hooks or suspicious privileges.
Application allowlisting and behavioral baselines for endpoints.
