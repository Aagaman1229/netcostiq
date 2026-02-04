# Netcostiq

Netcostiq is a Python-based project developed and tested on **Ubuntu Linux**.  
This repository contains only the **source code and configuration files**.  
Each user must create and use their **own virtual environment (venv)**.

---

## ⚠️ Important Notice

- This project is intended for **Ubuntu Linux only**
- Do **NOT** upload or use any `venv/` folder from GitHub
- Always create your own virtual environment
- Install dependencies using `requirements.txt`

---

## 🛠 Prerequisites

Make sure Python and pip are installed:

### Clone the repository
git clone https://github.com/Aagaman1229/netcostiq.git && \
cd netcostiq && \

### Create virtual environment
python3 -m venv venv && \

### Activate virtual environment
source venv/bin/activate && \

### Upgrade pip
pip install --upgrade pip && \

### Install dependencies
pip install -r requirements.txt


---
<br>

# About This Project: 
---

## 🌐 What is NetCostIQ?

NetCostIQ is a **network traffic cost intelligence system** that converts raw packet captures (PCAP) into **business-level cost insights**.


From a single PCAP file, NetCostIQ:
- Extracts network flows  
- Enriches them with business features  
- Scales them to real enterprise levels  
- Applies cost models (cloud, ISP, ingress/egress)  
- Generates reports, summaries, and dashboards  

---

## 🔁 End-to-End Pipeline

```text
PCAP → Flows → Enriched Flows → (Scaled) → Cost Model → Reports & Dashboard
```
| Stage | Script | Description |
| :--- | :--- | :--- |
| **Ingestion** | `pcap_to_flows.py` | Extracts raw flows from PCAP files. |
| **Enrichment** | `flow_enricher.py` | Adds metadata (Traffic Type, Timestamps). |
| **Scaling** | `real_scale.py` | Simulates enterprise-level data volume. |
| **Modeling** | `cost_model.py` | Applies NRS-based financial billing logic. |
| **Visuals** | `visual.py` / `dashboard.py` | Generates charts and interactive insights. |

---

## 📊 Business Insights (Example Results)

Based on our enterprise-scale simulation, NetCostIQ provides high-level financial metrics:

* **Total Flows Processed:** 253
* **Total Data Volume:** 548.51 GB
* **Total Calculated Cost:** NRS 27,308
* **Monthly Projection:** NRS 19,662,186
* **Peak Traffic Share:** 76.9% (Critical for cost optimization)

### Cost Distribution
Cloud Egress represents the highest financial leak (**~60%**), while internal traffic is correctly identified as **0 NRS**, validating the cost-logic accuracy.

---

## 🧪 Enterprise Scaling Logic
Since raw PCAP files are often small, NetCostIQ uses a `scale_factor` (e.g., $10^6$) to simulate the traffic of:
* Large Scale Enterprises
* ISPs / Universities
* High-traffic Cloud Workloads

This ensures the cost models reflect **realistic business magnitudes** rather than just home network traffic.

---
## 📁 Project Structure

```text
netcostiq/
├── src/
│   ├── pcap_to_flows.py      
│   ├── flow_enricher.py      
│   ├── real_scale.py         
│   ├── cost_model.py         
│   ├── visual.py             
│   └── dashboard.py          
├── data/
│   └── sample.pcap           
├── reports/                  
├── requirements.txt          
└── README.md
```
## 🚀 Quick Usage

After setting up the environment, run the pipeline scripts in order:

```bash
# 1. Extract flows from PCAP
python3 src/pcap_to_flows.py

# 2. Enrich with business features
python3 src/flow_enricher.py

# 3. Scale to enterprise levels
python3 src/real_scale.py

# 4. Calculate costs and generate reports
python3 src/cost_model.py

# 5. Generate visualizations (optional)
python3 src/visual.py

# 6. Launch interactive dashboard (optional)
streamlit run src/dashboard.py
```
## 📄 License

This project is open source and available for educational and research purposes. Feel free to use, modify, and distribute it for academic or personal learning.

