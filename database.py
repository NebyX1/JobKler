import certifi
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os



load_dotenv()


connection_string = os.environ['DB_CONNECTION']

connect_args = {
    "ssl": {
        "ca": certifi.where()
    }
}

engine = create_engine(connection_string, connect_args=connect_args)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        rows = result.all()
        print(rows)

    jobs = []
    for row in rows:
        job = {
            'id': row[0],
            'position': row[1],
            'city': row[2],
            'salary': row[3],
        }
        jobs.append(job)
    return jobs