import psycopg2
import pytest

def get_db_connection():
    return psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="localhost",
        port="5433"
    )

def test_database_connection():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="localhost",
        port="5433"
    )
    assert conn is not None

def test_data_insertion():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result[1] == 'John'

def fetch_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        assert len(rows) > 0, "No users found in the database"
        return rows
    except Exception as e:
        pytest.fail(f"Error during data fetch: {e}")
    finally:
        cursor.close()
        conn.close()

def test_fetch_users():
    users = fetch_users()
    assert len(users) > 0, "No users found"
    for user in users:
        assert len(user) == 2, "User data should have 2 columns (id and name)"
        assert isinstance(user[0], int), "User ID should be an integer"
        assert isinstance(user[1], str), "User name should be a string"


def test_update_data():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name='Jane' WHERE id=1")
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result is not None and result[1] == 'Jane'

def test_delete_data():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=1")
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result is None

if __name__ == "__main__":
    test_database_connection()
    test_data_insertion()
    fetch_users()
    test_update_data()
    test_delete_data()