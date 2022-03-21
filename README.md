# boats

### Стек
 - docker
 - redis
 - postgres
 - django
 - celery
 - drf

### Запуск приложения
- установить docker и docker-compose 
- положить xlsx файлы в директорию `files` 
- выполнить `make build && make up`
- для создания суперпользователя выполнить `make createadmin`

### API

#### Список судов
```
curl http://127.0.0.1:8000/api/vessels/ -u <creds>
```
#### Информация о судне по его коду
```
curl http://127.0.0.1:8000/api/vessels/<code>/ -u <creds>
```

#### Перемещения судна по его коду
```
curl http://127.0.0.1:8000/api/vessels/<code>/movements/ -u <creds>
```