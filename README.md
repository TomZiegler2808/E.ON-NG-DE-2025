# E.ON-NG-DE-2025
# 📝 Streamlit Note-Taking App

This project is a simple note-taking application built with Streamlit by a local SQLite database. It allows users to add and view notes through a clean web interface.

---

## 📦 Features

- Add notes with a title and content
- View all saved notes in reverse chronological order
- Notes are automatically timestamped
- Data is stored locally in a SQLite database (`notes.db`)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/streamlit-notes-app.git
cd streamlit-notes-app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize Database
```bash
python sqlite-db.py
```

### 4. Launch the App
```bash
streamlit run streamlit-app.py
```

---

## Known Issues
If the database is not initialized before running the app, you may encounter:
```
OperationalError: no such table: notes
```
To resolve this, run db_setup.py before launching the app.
Alternatively, a future improvement could be to create a main.py that handles both setup and app launch automatically.
