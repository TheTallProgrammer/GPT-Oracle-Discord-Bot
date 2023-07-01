import pymysql

def connect_to_database():
    # Replace these details with your actual database details
    conn = pymysql.connect(host='host',
                            user='user',
                            password='password',
                            db='db',
                            port=0000)
    return conn

def get_api_key(user_id):
    conn = connect_to_database()

    try:
        with conn.cursor() as cursor:
            query = "SELECT ApiKey FROM UserData WHERE UserID = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

    except Exception as e:
        print(e)
        return None

    finally:
        conn.close()

    if result:
        return result[0]
    else:
        return None

def save_api_key(user_id, api_key):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # SQL query to add the user ID and API key to the table
            sql = "INSERT INTO UserData (UserID, ApiKey) VALUES (%s, %s) ON DUPLICATE KEY UPDATE ApiKey=%s"
            cursor.execute(sql, (user_id, api_key, api_key))

        # commit the transaction
        conn.commit()

    except Exception as e:
        print(e)
        return False

    finally:
        conn.close()

    return True
