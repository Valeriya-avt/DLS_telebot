# DLS_telebot

## Стилизация изображений в телеграм-боте

Привет! Знакомьтесь с ботом, который умеет переносить стиль с одного изображения на другое:)

Что сделано:
- Написан код модели, которая может переносить стиль с одной фотографии на другую. Использован медленный алгоритм, за основу был взят [официальный туториал pytorch](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html),
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
docker stop dockername
```

### Удалить контейнер
```
docker rm dockername
```

### Примеры работы бота
Пример 1
![1](/docs/images/screenshot1.png)

![2](/docs/images/screenshot2.png)

![3](/docs/images/screenshot3.png)

Пример 2
![4](/docs/images/screenshot4.png)

![5](/docs/images/screenshot5.png)

![6](/docs/images/screenshot6.png)

Пример 3
![7](/docs/images/screenshot7.png)

![8](/docs/images/screenshot8.png)

![9](/docs/images/screenshot9.png)

