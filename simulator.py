"""
VIRUSS Laboratory - Script Analyzer & Security Sandbox
Provides safe inspection, static analysis, and signature detection for Windows Batch & VBS educational scripts.
"""

import os
import re
from typing import Dict, List

RISK_LEVELS = {
    "HIGH": "🔴 High Risk (Destructive / System Modification)",
    "MEDIUM": "🟡 Medium Risk (UI Annoyance / Loop Execution)",
    "LOW": "🟢 Low Risk (Educational / harmless demo)"
}

SCRIPT_CATALOG = [
    {
        "file": "PREVENT BOOTING VIRUS(del sys32).bat",
        "category": "Destructive Command (Simulation Only)",
        "risk": "HIGH",
        "description": "Attempts system file deletion (`del /f /s /q c:\\windows\\system32`).",
        "mitigation": "Windows User Account Control (UAC) & System File Protection (SFC) prevent unauthorized deletion."
    },
    {
        "file": "Shutdown PC virus.bat",
        "category": "System Power Action",
        "risk": "MEDIUM",
        "description": "Triggers local system shutdown (`shutdown -s -t 10`).",
        "mitigation": "Cancel shutdown immediately via command line using `shutdown -a`."
    },
    {
        "file": "enter key virus.vbs",
        "category": "Keystroke Injection / UI Loop",
        "risk": "MEDIUM",
        "description": "Uses VBScript WScript.Shell `SendKeys` to repeatedly send ENTER keys.",
        "mitigation": "Terminate the VBScript host process via Task Manager (`taskkill /f /im wscript.exe`)."
    },
    {
        "file": "Toogle capslock virus.vbs",
        "category": "Keystroke Loop",
        "risk": "MEDIUM",
        "description": "Repeatedly toggles the CapsLock key using `SendKeys`.",
        "mitigation": "Kill `wscript.exe` process."
    },
    {
        "file": "open multiple cmd virus.bat",
        "category": "Fork Bomb / Window Spawning",
        "risk": "MEDIUM",
        "description": "Spawns infinite Command Prompt instances (`:top start cmd goto top`).",
        "mitigation": "Close parent prompt or kill `cmd.exe` process tree."
    }
]

def analyze_script(filepath: str) -> Dict:
    """Perform static safety analysis on a script file."""
    if not os.path.exists(filepath):
        return {"error": f"File {filepath} not found."}
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    findings = []
    if re.search(r'del\s+.*system32', content, re.I):
        findings.append("CRITICAL: Destructive System32 deletion target detected!")
    if re.search(r'shutdown', content, re.I):
        findings.append("WARNING: System shutdown command detected.")
    if re.search(r'SendKeys', content, re.I):
        findings.append("NOTICE: Automated keystroke injection detected.")
    if re.search(r'goto\s+top|start\s+cmd', content, re.I):
        findings.append("WARNING: Infinite window spawning loop detected.")

    return {
        "file": os.path.basename(filepath),
        "size_bytes": len(content),
        "line_count": len(content.splitlines()),
        "findings": findings if findings else ["No high-risk keywords detected."]
    }

def main():
    print("==================================================")
    print("      VIRUSS EDUCATIONAL SECURITY ANALYZER        ")
    print("==================================================")
    print("[!] Educational & Defensive Research Suite Only.\n")

    for item in SCRIPT_CATALOG:
        print(f"📄 Script: {item['file']}")
        print(f"   Category:    {item['category']}")
        print(f"   Risk Rating: {RISK_LEVELS.get(item['risk'], item['risk'])}")
        print(f"   Behavior:    {item['description']}")
        print(f"   Mitigation:  {item['mitigation']}\n")

if __name__ == "__main__":
    main()
