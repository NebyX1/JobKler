from flask import Flask, render_template, request, redirect, url_for, flash
from database import load_jobs_from_db as get_all_jobs, load_job_from_db as get_job_by_id, add_application_to_db

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    jobs = get_all_jobs()
    return render_template('home.html', jobs=jobs)

@app.route('/job/<int:id>')
def job_detail(id):
    job = get_job_by_id(id)
    return render_template('jobpage.html', job=job)

@app.route('/job/<int:id>/apply', methods=['GET', 'POST'])
def apply_to_job(id):
    if request.method == 'POST':
        full_name = request.form.get('name', '').strip() or None
        email = request.form.get('email', '').strip() or None
        linkedin_url = request.form.get('linkedin', '').strip() or None
        education = request.form.get('education', '').strip() or None
        work_experience = request.form.get('work_experience', '').strip() or None

        add_application_to_db(id, full_name, email, linkedin_url, education, work_experience)

        return redirect(url_for('home'))
    else:
        return render_template('components/application_form.html', job_id=id)

if __name__ == '__main__':
    app.run(debug=True)