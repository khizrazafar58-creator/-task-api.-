# Task API

A small CRUD API for managing a to-do list, built with **FastAPI** (Python).
Built for the FlyRank AI Internship — Backend AI Engineering track — BE-01: *Build your first CRUD API*.

## What this is

A REST API with full CRUD (Create, Read, Update, Delete) operations on an in-memory list of tasks. Data lives in memory only — it resets when the server restarts (that's intentional; databases come in the next assignment).

## How to run it

1. Install Python 3.10+ if you don't have it: https://python.org
2. Install dependencies:
```bash
   pip install fastapi uvicorn
```
3. Start the server:
```bash
   uvicorn main:app --reload
```
4. The API is now running at `http://localhost:8000`
5. Interactive Swagger docs are automatically available at `http://localhost:8000/docs`

## Endpoints

| Method | Path | Description | Success | Errors |
|---|---|---|---|---|
| GET | `/` | API info | 200 | — |
| GET | `/health` | Health check | 200 | — |
| GET | `/tasks` | List all tasks | 200 | — |
| GET | `/tasks/{id}` | Get one task | 200 | 404 if not found |
| POST | `/tasks` | Create a task | 201 | 400 if title missing/empty |
| PUT | `/tasks/{id}` | Update a task | 200 | 404 if not found, 400 if body invalid |
| DELETE | `/tasks/{id}` | Delete a task | 204 | 404 if not found |
| GET | `/stats` | Task counts (extra) | 200 | — |
| POST | `/reset` | Reset to example tasks (extra) | 200 | — |

## Example: curl output
