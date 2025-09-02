import sqlite3


try:
    conn = sqlite3.connect("../db/magazines.db")
    cursor = conn.cursor()
    
    # Create publishers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)
    
    # Create magazines table (each magazine has one publisher)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )
    """)
    
    # Create subscribers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)
    
    # Create subscriptions table (links magazines to subscribers)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        magazine_id INTEGER,
        subscriber_id INTEGER,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id),
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id)
    )
    """)
    
    print("Tables created successfully!")
    conn.commit()
    
except sqlite3.Error as e:
    print(f"Error creating tables: {e}")
finally:
    if conn:
        conn.close()