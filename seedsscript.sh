python manage.py dumpdata auth.Group --indent 4 > seeds/auth_group.json
python manage.py dumpdata auth.User --indent 4 > seeds/auth_user.json
python manage.py dumpdata galeria.Categoria --indent 4 > seeds/galeria_categoria.json
python manage.py dumpdata galeria.Fotografia --indent 4 > seeds/galeria_fotografia.json