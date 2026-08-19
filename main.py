"""
Task API — a small CRUD API for managing a to-do list.
Built for FlyRank AI Internship — Backend AI Engineering — BE-01: Build your first CRUD API

Stage 0: hello server
Stage 1: root + health endpoints
Stage 2: read (list + single task, with 404)
Stage 3: create (POST, with 400 validation)
Stage 4: update + delete (PUT / DELETE)
Stage 5: Swagger UI — built in for free at /docs (FastAPI)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Task API",
    version="1.0",
    description="A small CRUD API for managing a to-do list. Built with FastAPI as part of the FlyRank AI Backend AI Engineering track."
)

# ---------------------------------------------------------------------------
# Stage 2: in-memory "database" — just a list, pre-filled with 3 example tasks
# ---------------------------------------------------------------------------
tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Finish FlyRank assignment", "done": False},
    {"id": 3, "title": "Walk the dog", "done": True},
]
next_id = 4  # simple counter for new task ids


# ---------------------------------------------------------------------------
# Request/response models
# ---------------------------------------------------------------------------
class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


# ---------------------------------------------------------------------------
# Stage 1: root + health endpoints
# ---------------------------------------------------------------------------
@app.get("/", tags=["meta"], summary="API info")
def root():
    """Describes this API and lists its main endpoint."""
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health", tags=["meta"], summary="Health check")
def health():
    """Simple health check — used to confirm the server is alive."""
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Stage 2: Read — list all tasks, or get a single task by id
# ---------------------------------------------------------------------------
@app.get("/tasks", tags=["tasks"], summary="List all tasks")
def list_tasks():
    """Returns every task currently stored."""
    return tasks


@app.get("/tasks/{task_id}", tags=["tasks"], summary="Get a single task")
def get_task(task_id: int):
    """Returns one task by id, or 404 if it doesn't exist."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


# ---------------------------------------------------------------------------
# Stage 3: Create — POST a new task, with validation
# ---------------------------------------------------------------------------
@app.post("/tasks", status_code=201, tags=["tasks"], summary="Create a new task")
def create_task(payload: TaskCreate):
    """
    Creates a new task. Requires a non-empty 'title'.
    Returns the created task with status 201.
    """
    global next_id
    title = payload.title.strip() if payload.title else ""
    if not title:
        raise HTTPException(status_code=400, detail="Title is required and cannot be empty")

    new_task = {"id": next_id, "title": title, "done": False}
    tasks.append(new_task)
    next_id += 1
    return new_task


# ---------------------------------------------------------------------------
# Stage 4: Update + Delete
# ---------------------------------------------------------------------------
@app.put("/tasks/{task_id}", tags=["tasks"], summary="Update a task")
def update_task(task_id: int, payload: TaskUpdate):
    """
    Updates a task's title and/or done status.
    Unknown id -> 404. Empty/invalid body -> 400.
    """
    for task in tasks:
        if task["id"] == task_id:
            if payload.title is not None:
                title = payload.title.strip()
                if not title:
                    raise HTTPException(status_code=400, detail="Title cannot be empty")
                task["title"] = title
            if payload.done is not None:
                task["done"] = payload.done
            if payload.title is None and payload.done is None:
                raise HTTPException(status_code=400, detail="Provide at least 'title' or 'done' to update")
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.delete("/tasks/{task_id}", status_code=204, tags=["tasks"], summary="Delete a task")
def delete_task(task_id: int):
    """Removes a task. Returns 204 with no body. Unknown id -> 404."""
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


# ---------------------------------------------------------------------------
# Optional extras (Stage "Make it yours")
# ---------------------------------------------------------------------------
@app.get("/stats", tags=["extras"], summary="Task statistics")
def stats():
    """Returns counts: total, done, open."""
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    return {"total": total, "done": done, "open": total - done}


@app.post("/reset", tags=["extras"], summary="Reset to example tasks")
def reset():
    """Restores the 3 original example tasks. Handy for demos."""
    global tasks, next_id
    tasks = [
        {"id": 1, "title": "Buy milk", "done": False},
        {"id": 2, "title": "Finish FlyRank assignment", "done": False},
        {"id": 3, "title": "Walk the dog", "done": True},
    ]
    next_id = 4
    return {"status": "reset", "tasks": tasks}
