FROM python:3.8 AS builder

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY creds /creds
COPY ChangeImageStyle_bot.py /
COPY pictures_processing.py /
COPY model.py /

CMD ["python3", "ChangeImageStyle_bot.py"]
