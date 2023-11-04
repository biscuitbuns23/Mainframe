python manage.py collectstatic --no-input

python manage.py migrate

gunicorn --worker-tmp-dir /dev/shm passdown_project2.wsgi

python manage.py tailwind start