# Forward bot

Это **бот-предложка**, все сообщения от пользователей пересылаются администратору как обычные форвард сообщения.

Бот очень компактный и имеет на борту только антифлуд.

Запуск контейнера:

    docker run -d \
    -e TG_ADMIN=YOUR_ID \
    -e TOKEN=BOT_TOKEN_FROM_BOTFATHER \
    --name memebot gentlemantleman/memebot

Так же можно изменить значение секунд таймера антифлуда (стандартное 5 секунд)

    docker run -d \
    -e TG_ADMIN=YOUR_ID \
    -e TOKEN=BOT_TOKEN_FROM_BOTFATHER \
    -e ANTIFLOOD=10 \
    --name memebot gentlemantleman/memebot

![Пример работы](https://i.ibb.co/NsJ8nQn/bbb.png)
