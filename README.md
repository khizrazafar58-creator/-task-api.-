# Task API

A beginner-friendly REST API for managing a to-do list, built with **FastAPI** and Python.

Built for the **FlyRank Internship — Backend Track — Week 2 — Assignment A1: Build Your First CRUD API**.

## What this is

A small REST API with full CRUD (Create, Read, Update, Delete) operations on an in-memory list of tasks.

Each task contains:

- `id` — number
- `title` — text
- `done` — true/false

The data is stored in memory only, so it resets when the server restarts. This is intentional because the assignment introduces databases in the following week.

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Swagger UI
- Git & GitHub

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
