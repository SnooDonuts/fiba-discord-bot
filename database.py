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
