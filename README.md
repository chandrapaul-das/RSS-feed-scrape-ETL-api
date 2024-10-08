# RSS Feed ETL FastAPI Service

This FastAPI application automates the extraction, classification, and storage of articles from RSS feeds. It fetches articles from provided RSS URLs, classifies them into categories using a machine learning model, and inserts them into an SQLite database.

## Features
- **Scrape articles** from RSS feeds.
- **Classify articles** into categories using a Naive Bayes model.
- **Insert articles** into an SQLite database with duplicate checks.

## Prerequisites

- Python 3.x installed
- SQLite database for storage
- Install dependencies from `requirements.txt`

## Installation
pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 5002 --reload


