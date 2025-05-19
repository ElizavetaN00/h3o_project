FROM python:3.11
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY app.py /usr/src/app/
EXPOSE 5002
CMD ["python", "/usr/src/app/app.py"]
