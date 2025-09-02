import sqlite3


try:
    conn = sqlite3.connect("../db/magazines.db")
    cursor = conn.cursor()

    # Create publishers table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """
    )

    # Create magazines table (each magazine has one publisher)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )
    """
    )

    # Create subscribers table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """
    )

    # Create subscriptions table (links magazines to subscribers)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        magazine_id INTEGER,
        subscriber_id INTEGER,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id),
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id)
    )
    """
    )

    print("Tables created successfully!")
    conn.commit()

except sqlite3.Error as e:
    print(f"Error creating tables: {e}")
finally:
    if conn:
        conn.close()


# Task3:
# Add these functions to your script


def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        return True
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists")
        return False


def add_magazine(cursor, name, publisher_name):
    # First find the publisher_id
    cursor.execute(
        "SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,)
    )
    result = cursor.fetchone()
    if result:
        publisher_id = result[0]
        try:
            cursor.execute(
                "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
                (name, publisher_id),
            )
            return True
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists")
            return False
    else:
        print(f"Publisher '{publisher_name}' not found")
        return False


def add_subscriber(cursor, name, address):
    # Check if subscriber already exists with same name and address
    cursor.execute(
        "SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address)
    )
    if cursor.fetchone():
        print(f"Subscriber {name} at {address} already exists")
        return False
    else:
        cursor.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address)
        )
        return True


def add_subscription(
    cursor, magazine_name, subscriber_name, subscriber_address, expiration_date
):
    # Find magazine_id
    cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
    magazine_result = cursor.fetchone()

    # Find subscriber_id
    cursor.execute(
        "SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?",
        (subscriber_name, subscriber_address),
    )
    subscriber_result = cursor.fetchone()

    if magazine_result and subscriber_result:
        magazine_id = magazine_result[0]
        subscriber_id = subscriber_result[0]

        # Check if subscription already exists
        cursor.execute(
            "SELECT * FROM subscriptions WHERE magazine_id = ? AND subscriber_id = ?",
            (magazine_id, subscriber_id),
        )
        if cursor.fetchone():
            print(
                f"Subscription already exists for {subscriber_name} to {magazine_name}"
            )
            return False
        else:
            cursor.execute(
                "INSERT INTO subscriptions (magazine_id, subscriber_id, expiration_date) VALUES (?, ?, ?)",
                (magazine_id, subscriber_id, expiration_date),
            )
            return True
    else:
        print("Could not find magazine or subscriber")
        return False


# Now use these functions to add data
try:
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key constraints
    cursor = conn.cursor()

    # Add publishers
    add_publisher(cursor, "Time Inc.")
    add_publisher(cursor, "Conde Nast")
    add_publisher(cursor, "Hearst Communications")

    # Add magazines
    add_magazine(cursor, "Time", "Time Inc.")
    add_magazine(cursor, "Sports Illustrated", "Time Inc.")
    add_magazine(cursor, "Vogue", "Conde Nast")

    # Add subscribers
    add_subscriber(cursor, "John Doe", "123 Main St")
    add_subscriber(cursor, "Jane Smith", "456 Oak Ave")
    add_subscriber(cursor, "Bob Johnson", "789 Pine Rd")

    # Add subscriptions
    add_subscription(cursor, "Time", "John Doe", "123 Main St", "2024-12-31")
    add_subscription(
        cursor, "Sports Illustrated", "Jane Smith", "456 Oak Ave", "2024-06-30"
    )
    add_subscription(cursor, "Vogue", "Bob Johnson", "789 Pine Rd", "2024-09-15")

    conn.commit()
    print("Data added successfully!")

except sqlite3.Error as e:
    print(f"Error adding data: {e}")
finally:
    if conn:
        conn.close()


# Task4

# Add this after your data insertion code

try:
    conn = sqlite3.connect("../db/magazines.db")
    cursor = conn.cursor()

    # Query 1: All subscribers
    print("\nAll subscribers:")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    # Query 2: Magazines sorted by name
    print("\nMagazines sorted by name:")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)

    # Query 3: Magazines for a specific publisher (Time Inc.)
    print("\nMagazines published by Time Inc.:")
    cursor.execute(
        """
    SELECT magazines.name 
    FROM magazines 
    JOIN publishers ON magazines.publisher_id = publishers.publisher_id 
    WHERE publishers.name = 'Time Inc.'
    """
    )
    for row in cursor.fetchall():
        print(row[0])  # Just print the magazine name

except sqlite3.Error as e:
    print(f"Error querying data: {e}")
finally:
    if conn:
        conn.close()
