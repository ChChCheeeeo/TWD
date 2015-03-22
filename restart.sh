rm -f 'db.sqlite3'
rm -rf './rango/migrations/'
#python manage.py clearsessions # clear cookies
python manage.py syncdb
python populate_rango.py
python manage.py syncdb
python manage.py makemigrations rango
python manage.py migrate
python manage.py runserver

