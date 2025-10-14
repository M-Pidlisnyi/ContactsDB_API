import psycopg

HOST = "localhost"
PORT = 5432
DB_NAME = "ContactsDB"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

def execute_query(query, params:tuple=(), fetch="none"):
    '''
    fetch can be:
        - "one"  → returns cursor.fetchone()
        - "all"  → returns cursor.fetchall()
        - "none" → returns nothing (must be used for INSERT/UPDATE/DELETE)
    '''
    try:
        with psycopg.connect(host=HOST, port=PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                if fetch == "one":
                    return cursor.fetchone()
                elif fetch == "all":
                    return cursor.fetchall()
                else:
                    connection.commit()
                    return None
                
    except psycopg.Error as e:
        print(f"Database error: {e}")
        return None
    

def create_contacts_table():
    execute_query('''
        CREATE TABLE IF NOT EXISTS contacts (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    description TEXT
                  );'''
                  )
    

if __name__ == "__main__":
    create_contacts_table()