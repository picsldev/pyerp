# PyERP
ERP en Django, Esto es un proyecto en Desarrollo.


# PIP
```
pip freeze > requirements.txt
```

# DJANGO
```
pip freeze > requirements.txt
python3 manage.py collectstatic
```

# MODELS
```
print %s%s' % (self.rut and ('[%s] ' % self.rut) or '', self.name)
print(self.rut + self.name)
```

# REINICIAR DJANGO
```
source /home/django/.venv/bin/activate
manage.py collectstatic
supervisor ctl restart django_app
```

# REINICIAR RSYNC
```
rsync -av db.sqlite3 root@ipdelservidor:/home/django/pyerp
```

# SERVER COMANDOS
```
cd pyerp
git pull
./manage.py collectstatic
```
