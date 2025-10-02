import streamlit as st
import sqlite3
from datetime import datetime

def add_note(title, content):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO notes (title, content, timestamp) VALUES (?, ?, ?)", (title, content, timestamp))
    conn.commit()
    conn.close()

def get_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, content, timestamp FROM notes ORDER BY timestamp DESC")
    notes = cursor.fetchall()
    conn.close()
    return notes

st.title("📝 Note Taking App")

st.header("Add a New Note")
title = st.text_input("Title")
content = st.text_area("Content")

if st.button("Save Note"):
    if title and content:
        add_note(title, content)
        st.success("Note saved successfully!")
    else:
        st.error("Please provide both title and content.")

st.header("Your Notes")
notes = get_notes()
if notes:
    for note in notes:
        st.subheader(note[0])
        st.write(note[1])
        st.caption(f"Saved on: {note[2]}")
        st.markdown("---")
else:
    st.info("No notes available yet.")
