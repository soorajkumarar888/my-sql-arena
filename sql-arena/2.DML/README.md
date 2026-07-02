# Data Manipulation Language (DML) Workflow

This directory orchestrates the complete Data Transformation and Ingestion workflow. It is broken down into a three-step pipeline:

## Folder Structure
1. **`1.source/`**: Contains the 4 raw `.csv` data files acting as the baseline source data required for the system database populate.
2. **`2.scripts/`**: Houses the custom `.py` Python files. These scripts act as the **Transformation (T)** engine of our ETL (Extract, Transform, Load) pipeline, parsing raw files and converting them safely into clean SQL injection syntax.
3. **`3.dml-output/`**: Stores the processed, bulk SQL `INSERT` statements produced dynamically by running the scripts.

## Core Setup Guide
* **The Full Walkthrough**: To understand or recreate the pipeline from scratch, follow the folders sequentially from `1` to `3`.
* **The Deployment Shortcut**: If you only need the final ready-to-use data payloads, skip directly into `3.dml-output/` and collect the processed SQL files.

*⚠️ **CRITICAL REMINDER**: Before executing any DML files found here, you **must** execute the master script located in the `1.DDL` folder first!*
