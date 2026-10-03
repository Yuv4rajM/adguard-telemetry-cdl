# AdGuard Telemetry Cloud Data Lake (CDL)

## 📌 Overview
This repository contains an end-to-end data engineering pipeline that extracts local network DNS telemetry from an AdGuard instance and ingests it into a Databricks-powered Cloud Data Lakehouse. 

The project demonstrates how to securely bridge on-premise network data with a cloud-native architecture using a hybrid Python/PySpark version-controlled workflow and a strict Medallion Architecture (Bronze, Silver, Gold).

## 🗂️ Repository Structure
* **`/src_extractor`**: A local Python API extraction client utilizing `requests` and `python-dotenv` to securely authenticate and pull raw DNS query logs from the local network.
* **`/databricks_cdl`**: Databricks PySpark notebooks that process the ingested data through the Medallion Data Lakehouse architecture.
* **`databricks.yml`**: Configuration for Databricks workspace deployment and CI/CD version control integration.

## 🏗️ Pipeline Architecture (Data Flow)

### 1. Ingestion & Extraction (Local to Cloud)
The Python client (`src_extractor`) queries the AdGuard REST API, handles authentication, and pushes the raw telemetry payload into the cloud data lake storage.

### 2. Medallion Data Lakehouse (`databricks_cdl`)
* **🥉 Bronze Layer (Raw):** Untransformed, raw telemetry data is landed in Delta format. Acts as an immutable historical archive and enables Change Data Capture (CDC).
* **🥈 Silver Layer (Cleansed):** PySpark scripts enforce schemas, filter out malformed network logs, standardize timestamps, and deduplicate network requests.
* **🥇 Gold Layer (Curated):** Business-level aggregations are built for BI visualization (e.g., aggregating blocked query counts by domain, tracking peak network traffic times, and identifying high-frequency client requests).

## 🛠️ Tech Stack
* **Compute & Orchestration:** Databricks, Apache Spark (PySpark)
* **Storage format:** Delta Lake
* **Extraction:** Python, REST APIs (`requests`), Environment Management (`dotenv`)
* **DevOps:** Git, Databricks Repos
