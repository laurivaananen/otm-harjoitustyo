import sqlite3


def get_database_connection():
    """
    Returns a database connection

    :return: Database connection
    :rtype: Connection
    """
    return sqlite3.connect("slack.db")


def create_command_table():
    """
    Creates a database table for regular expression triggers
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE command(id integer PRIMARY KEY,"
                   " command text, response text)")
    conn.commit()
    conn.close()


def create_tokens_table():
    """
    Creates a database for tokens
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE token(id integer PRIMARY KEY,"
                   " slack text, bot text)")
    conn.commit()
    conn.close()


def insert_token(oauth_token, bot_token):
    """
    Inserts oauth tokens in to the database

    :param str oauth_token: OAuth access token
    :param str bot_token: Bot user OAuth access token
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    possible = False
    cursor.execute("DELETE FROM token;")
    cursor.execute("INSERT INTO token(slack, bot) VALUES (?, ?)",
                   (oauth_token, bot_token))
    conn.commit()
    conn.close()


def insert_command(command, response):
    """
    Inserts a command, response pair into a database

    :param str command: Regular expression  to match a message received from Slack
    :param str response: Bot responds with this message
    :return: If it was possible to insert into the database
    :rtype: bool
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    possible = False
    # Add a command to database only if it doesn't exist
    if cursor.execute("SELECT EXISTS(SELECT 1 FROM command WHERE command = ?)",
                      (command,)).fetchone()[0] == 0:
        cursor.execute("INSERT INTO command(command, response) VALUES (?, ?)",
                       (command, response))
        possible = True

    conn.commit()
    conn.close()
    return possible


def delete_command(command):
    """
    Deletes a command from the database

    :param str command: Deletes this row from the database
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM command WHERE command.command = ?", (command,))
    conn.commit()
    conn.close()


def fetch_all_command_pairs():
    """
    Fetches all rows from database

    :return: All trigger, response pairs from database
    :rtype: dict
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    command_pairs = {row[1]: row[2] for row
                     in cursor.execute("SELECT * FROM command")}
    conn.close()
    return command_pairs


def fetch_token(token):
    """
    Fetches token from the database

    :param str token: The type of token to return
    :return: OAuth token
    :rtype: str
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    if token == "slack":
        token = cursor.execute("SELECT token.slack FROM token;").fetchone()
    elif token == "bot":
        token = cursor.execute("SELECT token.bot FROM token;").fetchone()

    if token:
        return token[0]
    else:
        print("Couldn't find token in the database. Make sure you have added it")
        return None
