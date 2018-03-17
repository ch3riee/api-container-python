 FROM python:3
 RUN mkdir /code
 ADD requirements.txt . 
 ADD djangoproj .
 RUN pip install -r requirements.txt
 RUN ln -s /code /temp
 CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
