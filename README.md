
# 🛡️ Sentinel-AI: Autonomous Cyber Defense Node

> **Status:** Active | **Version:** 1.0.0 | **Compliance:** Ethical/Passive

## 📖 Overview
Sentinel-AI is a next-generation threat intelligence tool designed to solve "Analysis Paralysis."

In 2025, security teams are drowning in raw logs. Finding data isn't the problem—understanding it is. Sentinel-AI automates this by using **Llama 3.3 (via SambaNova)** to analyze targets in real-time, providing actionable risk assessments and mitigation strategies instantly.

## 🧠 Tech Stack (The "Level 4" Architecture)
* **Core Intelligence:** Meta Llama 3.3 (70B) via SambaNova Systems
* **Reconnaissance:** Shodan API (Passive OSINT)
* **Threat Research:** Tavily AI Search (Real-time CVE Database)
* **Memory:** Supabase (PostgreSQL for immutable logging)
* **Frontend:** Streamlit Cloud

## ⚡ Key Features
* **🛡️ Passive Reconnaissance:** Maps network topology without sending active packets. It is undetectable by target firewalls.
* **🤖 AI Analyst:** Converts raw open port data into specific attack vector scenarios (e.g., distinguishing between a generic DNS server and a DDoS amplification node).
* **🌍 Visual Telemetry:** Interactive geospatial threat tracking.
* **🔒 Zero-Trust Architecture:** Evaluates targets based on technical configuration, not just reputation.

## ⚖️ Legal Disclaimer
This tool is engineered for **Passive Reconnaissance** only. It relies strictly on public API queries (Shodan) and does not initiate direct network connections to target infrastructure. It is fully compliant for educational and defensive research.


