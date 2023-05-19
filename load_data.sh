rm db.sqlite3
python manage.py migrate
python manage.py loaddata seeds/auth_group.json
python manage.py loaddata seeds/auth_user.json
python manage.py loaddata seeds/galeria_categoria.json
python manage.py loaddata seeds/galeria_fotografia.json