FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . /usr/src/app

# Install dependencies:
RUN pip install -r /usr/src/app/requirements.txt

CMD ["python", "main.py"]