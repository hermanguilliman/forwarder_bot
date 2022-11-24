# Forward bot

Это **бот-предложка**, все сообщения от пользователей пересылаются администратору как обычные форвард сообщения.

Бот очень компактный и имеет на борту только антифлуд.

Запуск контейнера c обязательными параметрами:

    docker run -d --restart=always\
    -e TG_ADMIN=YOUR_ADMIN_ID \
    -e TOKEN=BOT_TOKEN_FROM_BOTFATHER \
    -e PROMO=NAME_OF_YOUR_PROMO_CHANNEL \
    --name memebot gentlemantleman/memebot

С дополнительными параметрами:

    docker run -d --restart=always \
    -e TG_ADMIN=YOUR_ID \
    -e TOKEN=BOT_TOKEN_FROM_BOTFATHER \
    -e PROMO=NAME_OF_YOUR_PROMO_CHANNEL \
    -e ANTIFLOOD=5 \
    --name memebot gentlemantleman/memebot

![Пример работы](https://i.ibb.co/NsJ8nQn/bbb.png)
