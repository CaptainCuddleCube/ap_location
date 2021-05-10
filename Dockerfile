FROM python:3.9

WORKDIR /app

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY ap_location ap_location

CMD [ "gunicorn", "ap_location.main:app", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000" ]
