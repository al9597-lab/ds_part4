# NYU Database Systems – Project Part IV  
### AI Document Processing Pipeline with PostgreSQL Integration

---

## Overview
This project implements **Part IV** of the NYU Database Systems course project.

The goal is to:
1.Load unstructured health-related documents from PostgreSQL  
2.Run a pretrained **DistilBERT disease classification model**  
3.Predict patient risk and disease category  
4.Store AI inference results back into PostgreSQL  

This demonstrates how **Machine Learning integrates with database systems** in a real architecture.

---

## System Architecture
PostgreSQL (unstructured_document) → Python Pipeline → DistilBERT Model → PostgreSQL (document_inference)

---

## Project Structure
```
ds_part4
 ├─ app/
 │   ├─ config.py              # Loads environment variables
 │   ├─ db.py                  # Database engine & session
 │   ├─ model_inference.py     # Loads DistilBERT + prediction logic
 │   └─ pipeline.py            # Full ETL + inference pipeline
 ├─ models/
 │   └─ distilbert_chronic_disease/   # Local model folder (not pushed to GitHub)
 ├─ main.py
 ├─ requirements.txt
 └─ .env (ignored)
```

## Database Tables

### unstructured_document
doc_id (SERIAL PK)  
customer_id (INTEGER)  
content (TEXT)  
created_at (TIMESTAMP)

### document_inference
inference_id (SERIAL PK)  
doc_id  
predicted_disease  
risk_score  
model_version  
predicted_at  

---

## Environment Configuration
Create `.env` in project root:

PG_HOST=localhost  
PG_PORT=5432  
PG_USER=postgres  
PG_PASSWORD=******  
PG_DB=insdb  

MODEL_PATH=models/distilbert_chronic_disease  
MODEL_VERSION=distilbert_v1  

---

## Installation
pip install -r requirements.txt

---

## Run Pipeline
python main.py

Expected output:
Processing X documents...  
Pipeline completed.

---

## Verify Results in PostgreSQL
SELECT * FROM document_inference;

---

## Model Notes
Model is a **fine-tuned DistilBERT classifier**
Predicts:
Diabetes  
Cardiovascular Disease  
Respiratory Disease  

Model weights are **NOT uploaded to GitHub** due to size (>250MB)
They remain stored locally and are referenced via MODEL_PATH

---

## Team
NYU DS Project – Part IV  
Authors:
- Xiaoke Huang
- Ao Li
