
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
con = sqlite3.connect("users.db")
cur = con.cursor()

# Create a table for users if it doesn't already exist
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    balance INTEGER DEFAULT 100
)
''')

# Create a table for TODO items if it doesn't already exist
cur.execute('''
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    priority INTEGER NOT NULL,
    date TEXT NOT NULL,
    username TEXT,
    FOREIGN KEY(username) REFERENCES users(username) ON DELETE CASCADE
)
''')
con.commit()

# Function to initialize a new user with a default balance of 100
def createUser(username):
    try:
        cur.execute("INSERT INTO users (username, balance) VALUES (?, ?)", (username, 100))
        con.commit()
        print(f"User '{username}' created with a balance of 100.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")

# Function to check the balance of a user
def checkBalance(username):
    cur.execute("SELECT balance FROM users WHERE username = ?", (username,))
    result = cur.fetchone()
    if result:
        balance = result[0]
        return balance
    else:
        return None

# Function to update the balance of a user
def updateBalance(username, amount):
    current_balance = checkBalance(username)
    if current_balance is not None:
        new_balance = current_balance + amount
        cur.execute("UPDATE users SET balance = ? WHERE username = ?", (new_balance, username))
        con.commit()
        return new_balance
    return None

# Function to check if a user exists
def userExists(username):
    cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    return cur.fetchone() is not None

# Function to reset a user's balance to default (100)
def resetUser(username):
    if userExists(username):
        cur.execute("UPDATE users SET balance = 100 WHERE username = ?", (username,))
        con.commit()
        print(f"User '{username}' balance has been reset to 100.")
    else:
        print(f"User '{username}' does not exist.")

# --- Functions for managing TODO list ---

# Function to add a TODO item for a user
def addTodo(name, priority, date, username):
    cur.execute("INSERT INTO todos (name, priority, date, username) VALUES (?, ?, ?, ?)", (name, priority, date, username))
    con.commit()
    print(f"TODO item '{name}' added for user '{username}' with priority {priority}.")

# Function to remove a TODO item 
def removeTodo(name):
    cur.execute("DELETE FROM todos WHERE name = ?", (name,))
    con.commit()
    print(f"TODO item '{name}' was removed.")


# Function to update a TODO item for a user
def updateTodo(name, priority = None, date = None, username = None):
    cur.execute("UPDATE todos SET priority = ?, date = ? WHERE name = ? AND username = ?", (priority, date, name, username))
    con.commit()
    print(f"TODO item '{name}' updated for user '{username}'.")

# Function to get TODO items by username, date, or priority
def getTodos(username=None, date=None, priority=None):
    query = "SELECT name, priority, date, username FROM todos WHERE 1=1"
    params = []

    if username:
        query += " AND username = ?"
        params.append(username)
    if date:
        query += " AND date = ?"
        params.append(date)
    if priority:
        query += " AND priority = ?"
        params.append(priority)

    cur.execute(query, params)
    todos = cur.fetchall()
    return todos

# Function to get a TODO item by its name
def getTodoByName(name):
    cur.execute("SELECT name, priority, date, username FROM todos WHERE name = ?", (name,))
    todo = cur.fetchone()
    if todo:
        return {'name': todo[0], 'priority': todo[1], 'date': todo[2], 'username': todo[3]}
    return None

# Function to get all TODO items for all users
def getAllTodos():
    cur.execute("SELECT username, name, priority, date FROM todos")
    todos = cur.fetchall()
    return todos

