# Reflected XSS Scanner (Python)

A simple Python-based Reflected XSS scanner built as part of the VipraTech Security Engineer (Python – Tooling & Integrations) assignment.

The scanner:
- Accepts a target URL and parameters  
- Injects dynamically generated payloads  
- Supports multiple injection contexts  
- Sends GET and POST requests  
- Detects reflected payloads in responses  
- Produces an HTML report showing where reflections were found  

This project is intentionally minimal and beginner-friendly, focusing on clarity over complexity.

---

## 🛠 Features (Meets Assignment Requirements)

### ✔ Python implementation  
### ✔ PayloadGenerator class  
Generates context-based payloads for:
- **text context**
- **attribute-value**
- **attribute-name** (mandatory per assignment)

### ✔ Reflected XSS detection  
A simple substring match verifies whether the injected payload appears in the response.

### ✔ Supports GET and POST methods  
### ✔ HTML reporting  
A clean, readable `report.html` file is generated with reflections found.

### ✔ Modular architecture  
- `payloads.py` – Context-based payload generator  
- `scanner.py` – HTTP request sender & reflection detector  
- `reporter.py` – HTML report builder  
- `run.py` – Main entry point  

---

## 📂 Project Structure

