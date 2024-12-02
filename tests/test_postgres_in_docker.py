import psycopg2

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