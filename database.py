import certifi
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from datetime import datetime

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

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {'val': id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            row = rows[0]
            job = {column: value for column, value in zip(result.keys(), row)} 
            return job
        
def add_application_to_db(job_id, full_name, email, linkedin_url, education, work_experience):
    with engine.connect() as conn:
        current_time = datetime.utcnow()
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, created_at, updated_at) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :created_at, :updated_at)")
        conn.execute(query.bindparams(job_id=job_id, full_name=full_name, email=email, linkedin_url=linkedin_url, education=education, work_experience=work_experience, created_at=current_time, updated_at=current_time))