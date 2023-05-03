![example workflow](https://github.com/vartexxx/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

Проект доступен по этому IP: 178.154.204.85
### Описание
Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Igor-L12/yamdb_final.git
```

```
cd infra
```

Развернуть докер контейнеры:
```
sudo docker-compose up
```

Выполнить миграции и собрать статику
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
### Примеры использования api:
Получение произведений:
```
GET /api/v1/titles/
```
Добавление произведения (только администратор):
```
POST /api/v1/titles/
```
В параметрах передавать json
```
{
    "name": "Название произведения",
    "year": 1995,
    "description": "Описание произведения",
    "genre": [
    "comedy"
    ],
    "category": "films"
}
```
