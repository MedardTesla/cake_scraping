# 🍽️ Data engineering project for cakes

Welcome to the cakes **Data Engineering project**!
This project demonstrates a complete data pipeline that extracts recipe data from a public website, processes it with Apache Airflow, stores it in Azure Data Lake, transforms and migrates it with Azure Data Factory, queries it via Azure Synapse Analytics, and finally visualizes insights using Tableau.



## 🚀 Project Overview

This project follows the full data pipeline lifecycle:

1. **Extraction**: We scrape recipe data from a website using Python and orchestrate the process using **Apache Airflow**.
2. **Storage**: Extracted data is stored in **Azure Data Lake Storage (ADLS)** as JSON or Parquet.
3. **Migration**: Data is transferred and transformed using **Azure Data Factory (ADF)** pipelines.
4. **Analytics**: We run queries on structured data using **Azure Synapse** to create analytical datasets.
5. **Visualization**: Finally, the processed data is visualized using **Tableau** dashboards for insights.

## Table of Contents


1. System Architecture
2. Requirements
3. Getting Started
4. Running the Code With Docker

## System Architecture
![system architecture](https://github.com/MedardTesla/cake_scraping/blob/main/data/Diagramme%20sans%20nom.png)

## Requirements

- Python 3.9 (minimum)
- Docker
- PostgreSQL
- Apache Airflow 3.0.0 (minimum)

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/MedardTesla/cake_scraping.git
cd cake_scraping
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Start your services on Docker with

```bash
docker compose up airflow-init
docker compose up
```




