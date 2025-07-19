 Performance & Readability Gains
🚀 Reduced Repetition: Common DB operations moved to helpers.py

🧠 Cleaner Routes: Logic is separated from route functions → easier to read

💨 Faster DB Access: Used db.get() which is simpler than .filter_by().first() for primary keys

🔐 Safer Input: Basic input validation prevents empty task creation

📂 Modular Design: Easier to maintain and scale in the future

Add Task	✅
View Tasks	✅
Toggle Done	✅
Delete Task	✅
Empty Input	✅ Handled

