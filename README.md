# dipy_web
Website generation and content management tools for dipy.org


```python
pip install -r requirement-dev.txt

cp dipy_web/settings.py.example dipy_web/settings.py

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py createsuperuser
python manage.py runserver
```
