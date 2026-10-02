# VIRUSS: Educational Cyber Security & Batch Scripting Laboratory

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://www.python.org/)
[![Security Lab](https://img.shields.io/badge/Security-Educational%20Lab-red.svg)](simulator.py)
[![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

**VIRUSS Laboratory** is an educational security research repository housing legacy Windows Batch and VBScript mechanics, static code analyzers, process isolation simulators, and defensive mitigation documentation.

---

## 🔬 Laboratory Inventory & Analysis

| Script File | Target Mechanism | Risk Rating | Remediation & Defense |
| :--- | :--- | :--- | :--- |
| `PREVENT BOOTING VIRUS(del sys32).bat` | System Deletion Target | 🔴 High | System File Protection (SFC) & UAC privilege escalation boundaries. |
| `Shutdown PC virus.bat` | Power State Trigger | 🟡 Medium | Abort pending shutdown using `shutdown -a` in CMD. |
| `enter key virus.vbs` | Keystroke Injection Loop | 🟡 Medium | Kill process via `taskkill /f /im wscript.exe`. |
| `Toogle capslock virus.vbs` | Key State Injection | 🟡 Medium | Kill process via `taskkill /f /im wscript.exe`. |
| `open multiple cmd virus.bat` | Window Spawning Loop | 🟡 Medium | Terminate process tree via Task Manager or CMD. |

---

## 🚀 Quick Start

### 1. Launch Web Research Sandbox
Open [`index.html`](index.html) in any web browser to view interactive payload breakdowns, risk levels, and defensive remedies.

### 2. Run Python Static Security Analyzer
```bash
python simulator.py
```

---

## 🛡️ Governance & Safety Policy

- **[Code of Conduct](CODE_OF_CONDUCT.md)**
- **[Contributing Guide](CONTRIBUTING.md)**
- **[Security Policy](SECURITY.md)**
- **[License](LICENSE)**
