import sqlite3

DB_NAME = "streetlight.db"


def create_database():
    """
    Creates the SQLite database and the street_lights table if they do not exist.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create the street_lights table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS street_light (
                light_id TEXT PRIMARY KEY,
                area_name TEXT,
                pole_number TEXT,
                latitude REAL,
                longitude REAL,
                installation_date TEXT,
                status TEXT
            )
        """)

        # Save changes
        conn.commit()
        conn.close()

        print("Database and table created successfully.")

    except sqlite3.Error as e:
        print(f"Error creating database: {e}")


def add_street_light(light_id, area_name, pole_number,
                      latitude, longitude,
                      installation_date, status):
    """
    Adds a new street light record to the database.
    """

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO street_light (
                light_id,
                area_name,
                pole_number,
                latitude,
                longitude,
                installation_date,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            light_id,
            area_name,
            pole_number,
            latitude,
            longitude,
            installation_date,
            status
        ))

        conn.commit()
        print("Street Light Registered Successfully.")

    except sqlite3.IntegrityError:
        print("Street Light ID already exists.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        conn.close()
def view_all_light():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM street_light")
        records = cursor.fetchall()

        if records:
            print("\n--- Street Light Records ---")
            for record in records:
                print(record)
        else:
            print("No street lights found.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        conn.close()
def search_street_light(light_id):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM street_light WHERE light_id = ?",
            (light_id,)
        )

        record = cursor.fetchone()

        if record:
            print("\n===== STREET LIGHT DETAILS =====")
            print(f"Light ID: {record[0]}")
            print(f"Area Name: {record[1]}")
            print(f"Pole Number: {record[2]}")
            print(f"Latitude: {record[3]}")
            print(f"Longitude: {record[4]}")
            print(f"Installation Date: {record[5]}")
            print(f"Status: {record[6]}")
        else:
            print("Street Light not found.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        conn.close()
if __name__ == "__main__":
    create_database()