import os

from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


@app.route('/')
def index():
    record = 'No records found...'
    connection = None
    try:
        DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://folkol@localhost:5432/planning-tool')
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")
        # Print PostgreSQL version
        cursor.execute("SELECT * FROM activities")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return str(record or 'No records found...')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)


