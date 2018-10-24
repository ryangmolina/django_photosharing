```
sudo docker images -a
sudo docker-compose run web python /photosharing_site/manage.py makemigrations --noinput
sudo docker-compose up -d --build

sudo docker-compose exec web bash
```
