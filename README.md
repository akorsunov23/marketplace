# Интернет-магазин MEGANO
Владелец торгового центра во время COVID-карантина решил перевести своих арендодателей в онлайн. Сделать это он намерен с помощью создания платформы, на которой продавцы смогут разместить информацию о себе и своём товаре. Онлайновый торговый центр или, другими словами, интернет-магазин, являющийся агрегатором товаров различных продавцов.

## Как установить
Для работы микросервиса нужен Python версии не ниже 3.10.    

Настройка переменных окружения  
1. Склонируйте репозиторий
```shell
git clone https://github.com/akorsunov23/marketplace.git
``` 
2. Создайте файл .env. и заполните его по примеру env.dist

3. Установка виртуального окружения для среды разработки и установите зависимости
 - на примере ОС Windows
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements\dev.txt
```
 - на примере ОС Linux
```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements/base.txt
```
4. Запустите локальный сервер
```shell
python manage.py runserver
``` 
## Проверка форматирования кода
Проверка кода выполняется из корневой папки репозитория.    
* Анализатор кода flake8  
```shell
flake8
```
* Линтер pylint  
```shell
pylint --rcfile=.pylintrc market/* 
```

# Цели проекта

Код написан в учебных целях — это курс по Джанго на сайте [Skillbox](https://go.skillbox.ru/education/course/django-framework).  

### Быстрый тест:

Для быстрого тестирования необходимо загрузить фикстуры.
Загрузка данных в модели выполняется из папки `market/` следующей командой:

```shell
python manage.py loaddata fixtures/*.json
```

#### Данные cуперпользователя:

email: admin@admin.ru password: admin

#### Данные зарегистрированных пользователей:

1. email: david@test.ru password: 1304test
2. email: kevin@test.ru password: 1304test
3. email: robert@test.ru password: 1304test
4. email: skott@test.ru password: 1304test

#### Данные зарегистрированных пользователей, у которых есть магазин:

1. email: kenneth@test.ru password: 1304test
2. email: willard@test.ru password: 1304test
3. email: kyle@test.ru password: 1304test
4. email: glenn@test.ru password: 1304test
5. email: keith@test.ru password: 1304test  


### Приложение imports:

Команды для выполнения импорта:

- выполнения импорта всех файлов
````shell
python manage.py imports all
````
- выполнения импорта одного файла
````shell
python manage.py imports <имя файла>
````
- выполнения импорта нескольких файлов
````shell
python manage.py imports <имена файлов через пробел>
````

#### CELERY

Также импорт можно поставить на периодическое выполнение задачи.
Для настройки времени периодов выполнения задач необходимо задать требуемые параметры 
в админ панели, подробнее можно посмотреть в статье [Сергея Климова](https://habr.com/ru/articles/711590/).

Команды запуска выполнения задач в фоновом режиме:

- Запуск брокера сообщений Redis
````shell
redis-server
````
- Запуск Celery для выполнения задачи по импорту
````shell
celery -A config worker -l info
````
- Запускаем службу beat
````shell
celery -A config beat -l info
````
- Запускаем сервер
````shell
python manage.py runserver
````


#### Система оплаты Stripe

Система оплаты настроена на тестовый режим!

Номер карты для тестирования оплаты - 
4242 4242 4242 4242 4242, остальные данные рандомные.

Для доступа к платёжной системе, необходимо зарегистрироваться на сервисе и после получение API ключей добавить в .env:
- STRIPE_SECRET_KEY = секретный ключ
- STRIPE_PUBLISHABLE_KEY = публичный ключ

[![2023-06-15-23-22-56.png](https://i.postimg.cc/nrRkS4vm/2023-06-15-23-22-56.png)](https://postimg.cc/XB5dpy1N)

- STRIPE_WEBHOOK_KEY = ключ веб перехвадчика

Инструкции по настройке и получения ключа webhook можно почитать в официальной документации [сервиса](https://stripe.com/docs/stripe-cli#install)

#### Почта SMPT

Сервис отправки электронных писем настроен на сервере Google:

- EMAIL_HOST_USER = имя пользователя
- EMAIL_HOST_PASSWORD = пароль полученный при оформлении двухэтапной аутентификации