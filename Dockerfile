FROM python:3.8-slim
COPY dsproject.py dsproject.py
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt 
RUN chmod +x dsproject.py
ENTRYPOINT ["./dsproject.py"]
