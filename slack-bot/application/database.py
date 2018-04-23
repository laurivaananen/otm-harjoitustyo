import sqlite3

def get_database_connection():
    return sqlite3.connect("slack.db")

def create_command_table():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE command(id integer PRIMARY KEY, command text, response text)")
    conn.commit()
    conn.close()

def insert_command(command, response):
    conn = get_database_connection()
    cursor = conn.cursor()
    possible = False
    # Add a command to database only if it doesn't exist
    if cursor.execute("SELECT EXISTS(SELECT 1 FROM command WHERE command = ?)", (command,)).fetchone()[0] == 0:
        cursor.execute("INSERT INTO command(command, response) VALUES (?, ?)", (command, response))
        possible = True

    conn.commit()
    conn.close()
    return possible

def delete_command(command):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM command WHERE command.command = ?", (command,))
    conn.commit()
    conn.close()

def fetch_all_command_pairs():
    conn = get_database_connection()
    cursor = conn.cursor()
    command_pairs = {row[1]: row[2] for row in cursor.execute("SELECT * FROM command")}
    conn.close()
    return command_pairs
