Start rabbitmq from docker image

```
docker run -d --name my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

u-guest
p-guest

for django

```
python manage.py runserver
```

for django app as a consumer

```
python manage.py consumer
```

for flask

```
python app.py
```
