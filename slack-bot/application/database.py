import sqlite3

def get_database_connection():
    return sqlite3.connect("slack.db")

def create_command_table():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE command(command text, response text)")
    conn.commit()
    conn.close()

def insert_command(command, response):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO command(command, response) VALUES (?, ?)", (command, response))
    conn.commit()
    conn.close()

def fetch_all_command_pairs():
    conn = get_database_connection()
    cursor = conn.cursor()
    command_pairs = [(row[0], row[1]) for row in cursor.execute("SELECT command.command AS command, command.response AS response FROM command")]
    conn.close()
    return command_pairs