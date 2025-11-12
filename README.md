Educational Keystroke Logger — Lab / Defensive Demo
Short description
Educational keystroke-capture proof-of-concept intended strictly for defensive research and lab testing. Demonstrates basic keyboard event logging to a local file so security teams can study detection and remediation. Run only on systems you own or with explicit written permission.
CRITICAL — Read Before Using
This repository is for educational and defensive purposes only. Do not use on computers you do not own or without explicit written consent. Unauthorized use is illegal and unethical. The project purpose is to teach defenders how such tools work and how to detect and mitigate them.
Table of Contents
Purpose
Features
Requirements
Installation
Usage
Sanitized Example Output
File structure
Safe Lab Setup (recommended)
Detection & Remediation Guidance
Contribution Guidelines
Cleanup & Reversion
License & Disclaimer
Contact
Purpose
This repository demonstrates how keyboard-event capture can be implemented in a minimal, easy-to-follow way so that security practitioners can:
Understand how keystroke-capture works at a conceptual level.
Create controlled lab exercises for detection and response training.
Test detection rules and endpoint protections in isolated environments.
Not intended for abuse. The repository intentionally avoids any instructions or features for stealth, exfiltration, persistence, or remote attack.
Features
Minimal proof-of-concept script that records key events with timestamps to a local file.
Sanitized example logs and screenshots for demonstration.
Guidance on safe lab operation and detection strategies for defenders.
Requirements
Python 3.8+
pynput (or other standard input-listening library used by the included script)
Virtual machine or isolated test environment recommended
Installation
Clone the repository:
git clone https://github.com/[your-account]/[repo-name].git
cd [repo-name]
Create and activate a virtual environment (recommended):
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
requirements.txt example:
pynput
Usage (Lab / Defensive)
Only run this on systems you own or where you have explicit written consent.
Start the script in a terminal:
python keylogger.py
Interact with the system (or test pages) while monitoring from your isolated VM.
Stop the script with Ctrl+C and inspect the sanitized log file:
cat key_log.txt
Note: This repository does not include any automated exfiltration or deployment tooling.
