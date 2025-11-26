from datetime import datetime
import math

def calculate_priority(task, all_tasks, strategy="smart"):
    now = datetime.now().date()

    # --- Defensive defaults ---
    importance = int(task.get("importance", 5))
    effort = max(1, int(task.get("estimated_hours", 1)))
    due_date = task.get("due_date")

    # --- Urgency ---
    urgency_score = 0
    if due_date:
        try:
            due = datetime.strptime(due_date, "%Y-%m-%d").date()
            days_left = (due - now).days
            if days_left < 0:
                urgency_score = 10  # overdue
            else:
                urgency_score = max(0, 10 - days_left)
        except:
            urgency_score = 0

    # --- Dependency impact ---
    dependent_tasks = [
        t for t in all_tasks if task.get("id") in t.get("dependencies", [])
    ]
    dependency_score = len(dependent_tasks) * 2

    # --- Strategy switch ---
    if strategy == "fast":
        score = (10 / effort) + urgency_score
    elif strategy == "impact":
        score = importance * 2
    elif strategy == "deadline":
        score = urgency_score * 2
    else:  # smart balance
        score = (
            urgency_score * 0.4 +
            importance * 0.4 +
            (10 / effort) * 0.1 +
            dependency_score * 0.1
        )

    return round(score, 2)
