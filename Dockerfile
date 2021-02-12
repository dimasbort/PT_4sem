FROM python:3.8
COPY file.py /tmp/
CMD ["python", "/tmp/file.py"]
