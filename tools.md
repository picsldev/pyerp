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

# TRASLATE RUN
```
django-admin makemessages -l es_ES
```

# SERVER COMANDOS
```
cd pyerp
git pull
./manage.py collectstatic
```

# GIT
```
git checkout -b fixing_url_name_space
git pull origin fixing_url_name_space
git add .
git commit -m "Cambios en Rama"
git push origin fixing_url_name_space
```

# Miro las ramas (la activa es verde *)
```
git branch
```

# Crear una rama y de paso cambia a esa rama
```
git checkout -b nombreramma
```

#
```
git commit -am "Dañando cosas."
```

# 
```
git push origin nombreramma 
```

# uniendo ramas me paro en master y me traigo lo que tenia en nombre ramma
```
git checkout master
git merge nombreramma
```
