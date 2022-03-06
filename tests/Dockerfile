FROM python:3.7

WORKDIR /app

COPY . .

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 7979

CMD ["python3", "tests.py"]
