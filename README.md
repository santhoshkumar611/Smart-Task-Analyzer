# 🧠 Smart Task Analyzer

A mini task management system that intelligently **scores and prioritizes tasks** based on urgency, importance, effort, and dependencies.
Built as part of the **Software Development Intern Technical Assessment**.

---

## 📌 Problem Overview

Modern task lists often fail because they treat all tasks equally. This project addresses that by introducing a **smart prioritization engine** that helps users decide *what to work on first*.

The system analyzes tasks using multiple weighted factors and produces:

* A **priority score** for each task
* A **sorted list** of tasks
* A **human-readable explanation** for why each task is prioritized

---

## 🛠 Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Frontend:** HTML, CSS, Vanilla JavaScript
* **Database:** SQLite (default Django setup)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/santhoshkumar611/Smart-Task-Analyzer
cd Singularium_internship
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install django djangorestframework django-cors-headers
```

### 4. Run migrations

```bash
cd backend
python manage.py migrate
```

### 5. Start backend server

```bash
python manage.py runserver
```

### 6. Run frontend

Open `frontend/index.html` directly in the browser.

---

## 🔌 API Endpoints

### 1️⃣ Analyze Tasks

**POST** `/api/tasks/analyze/?strategy=smart`

* Accepts a JSON list of tasks
* Returns tasks sorted by priority score
* Includes explanation for each task

### 2️⃣ Suggest Tasks

**POST** `/api/tasks/suggest/?strategy=smart`

* Returns **top 3 tasks** to work on
* Includes clear reasoning for suggestions

---

## 🧮 Priority Scoring Algorithm (Core Logic)

Each task’s priority is calculated using a **weighted scoring model** that balances multiple factors:

### 1. Urgency

* Calculated from the due date
* Tasks closer to or past the deadline score higher
* Overdue tasks are heavily penalized

### 2. Importance

* User-defined scale from 1–10
* Higher importance directly increases the score

### 3. Effort (Quick Wins)

* Lower estimated hours receive higher weight
* Encourages completing impactful tasks quickly

### 4. Dependencies

* Tasks that block other tasks gain additional priority
* Helps unblock future work

### 5. Strategy-Based Weighting

The system supports multiple prioritization strategies:

* **Fastest Wins:** Favors low-effort tasks
* **High Impact:** Favors importance above all
* **Deadline Driven:** Favors urgency
* **Smart Balance:** Balanced weighting of all factors

The default “Smart Balance” strategy uses weighted contributions to avoid extreme prioritization and mimic real-world decision-making.

---

## 🧠 Explainability (Critical Thinking)

Each task includes a **human-readable explanation**, such as:

* *High importance*
* *Low effort*
* *Approaching deadline*
* *Blocks other tasks*

This makes the algorithm **transparent and defensible**, rather than a black box.

---

## 🧪 Edge Cases Handled

* Missing or invalid fields (safe defaults applied)
* Tasks without due dates
* Overdue tasks
* Low-effort but low-importance tasks
* Dependency chains
* Invalid request payloads (validated at API level)

---

## 🧪 Unit Tests

Basic unit tests are included to validate:

* High priority for overdue tasks
* Increased score for low-effort tasks
* Dependency-based priority boost

---

## ⏱ Time Breakdown

| Task                | Time        |
| ------------------- | ----------- |
| Backend setup & API | ~1.5 hours  |
| Scoring algorithm   | ~45 minutes |
| Frontend UI         | ~45 minutes |
| Debugging & testing | ~45 minutes |
| Documentation       | ~45 minutes |

---

## 🔮 Future Improvements

* Circular dependency detection with visualization
* Eisenhower Matrix (Urgent vs Important) view
* User-configurable weighting preferences
* Holiday/weekend-aware urgency calculation
* Learning-based prioritization using feedback

---

## ✅ Conclusion

This project demonstrates:

* Strong **problem-solving skills**
* Clean and readable **backend API design**
* Thoughtful **algorithmic decision-making**
* Practical **frontend integration**
* Clear and professional **documentation**

---

