from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .scoring import calculate_priority


@csrf_exempt
@api_view(["POST"])
def analyze_tasks(request):
    tasks = request.data

    # ✅ Validate input
    if not isinstance(tasks, list):
        return Response(
            {"error": "Expected a list of tasks"},
            status=status.HTTP_400_BAD_REQUEST
        )

    strategy = request.query_params.get("strategy", "smart")

    for task in tasks:
        task["score"] = calculate_priority(task, tasks, strategy)

        # ✅ Build explanation
        reasons = []

        if task.get("importance", 0) >= 7:
            reasons.append("High importance")

        if task.get("estimated_hours", 10) <= 3:
            reasons.append("Low effort")

        if task.get("due_date"):
            reasons.append("Approaching deadline")

        if task.get("dependencies"):
            reasons.append("Blocks other tasks")

        task["reason"] = ", ".join(reasons) if reasons else "Balanced priority"

    sorted_tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)
    return Response(sorted_tasks, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def suggest_tasks(request):
    tasks = request.data

    # ✅ Validate input
    if not isinstance(tasks, list):
        return Response(
            {"error": "Expected a list of tasks"},
            status=status.HTTP_400_BAD_REQUEST
        )

    strategy = request.query_params.get("strategy", "smart")

    for task in tasks:
        task["score"] = calculate_priority(task, tasks, strategy)

        # ✅ Clear reason for suggestion
        task["reason"] = "Suggested based on urgency, importance, and effort balance"

    top_three = sorted(tasks, key=lambda x: x["score"], reverse=True)[:3]
    return Response(top_three, status=status.HTTP_200_OK)
