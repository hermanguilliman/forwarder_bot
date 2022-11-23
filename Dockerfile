FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt ./app
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./app
ENV ANTIFLOOD=5
CMD [ "python", "./bot.py" ]