import sqlite3
import random

conn = sqlite3.connect('discord_bot.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS bored_messages(
            ID INTEGER PRIMARY KEY NOT NULL,
            message text
            )""")

def insert_msg(message_given):
    with conn:
        c.execute("SELECT * FROM 'bored_messages' WHERE message = ?", (' '.join(message_given),))
        is_command_in_database = c.fetchone()

        if is_command_in_database is None:
            c.execute("INSERT INTO 'bored_messages'(message) VALUES (?) ", (' '.join(message_given),))
            response = 0
        else:
            response = 1

        return response

def get_message():
    with conn:
        c.execute("SELECT * FROM 'bored_messages' WHERE ID = ?", (random.randint(1, 2),))
        test_if_in_database = c.fetchone()

        if test_if_in_database:
            print(test_if_in_database)

get_message()