FROM python:3
RUN pip install flask
EXPOSE 5000
ADD app.py /
#ENV FLASK_APP app.py
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
