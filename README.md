# DLS_telebot
---------------
## Стилизация изображений в телеграм-боте

Привет! Знакомьтесь с ботом, который умеет переносить стиль с одного изображения на другое:)

Что сделано:
- Написан код модели, которая может переносить стиль с одной фотографии на другую. Использован медленный алгоритм, за основу был взят официальный туториал pytorch [],
- создан бот, которому можно отправить две фотографии и получить в ответ фото с перенесенным стилем,
- упаковано в докер.

### Как скачать
```
git clone https://github.com/Valeriya-avt/DLS_telebot
```

### Как задать токен
Сохраните его в файл `./creds/ChangeImageStyle_bot.txt`

### Как запустить
Из корневого каталога запустите в терминале:
```
python ChangeImageStyle_bot.py
```

### Как запустить в докере
```
docker build -t bot .
docker run bot
```

### Остановить контейнер
```
docker stop bot
```

### Удалить контейнер
```
docker rm bot
```

Примеры работы бота:
![Alt text](/docs/images/screenshot1.png)

![Alt text](/docs/images/screenshot2.png)

![Alt text](/docs/images/screenshot3.png)

![Alt text](/docs/images/screenshot4.png)

![Alt text](/docs/images/screenshot5.png)

![Alt text](/docs/images/screenshot6.png)

![Alt text](/docs/images/screenshot7.png)

![Alt text](/docs/images/screenshot8.png)

![Alt text](/docs/images/screenshot9.png)

