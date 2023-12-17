# cv_reader
Python Flask application that presents your CV data

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt


Run the REST API: flask run or python app.py


The API will be accessible at http://127.0.0.1:5000/.

Personal Information: http://127.0.0.1:5000/personal
Experience: http://127.0.0.1:5000/experience
Education: http://127.0.0.1:5000/education
Skills: http://127.0.0.1:5000/skills

Run the application to print in the console:
export FLASK_APP=app.py
flask cv print

