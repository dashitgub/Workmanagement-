import subprocess
from django.db import connection
from django.test import Client
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def check_migrations():
    try:
        subprocess.check_call(['python3', 'manage.py', 'makemigrations'])
        subprocess.check_call(['python3', 'manage.py', 'migrate'])
        print("Миграции выполнены успешно.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка миграции: {e}")

def check_tables():
    tables = connection.introspection.table_names()
    if 'analiz_task' in tables:
        print("Таблица 'analiz_task' найдена в базе данных.")
    else:
        print("Таблица 'analiz_task' не найдена в базе данных. Проверьте миграции.")

def check_urls():
    client = Client()
    urls_to_check = [
        '/',
        '/analiz/',
        '/analiz/add/',
    ]
    
    for url in urls_to_check:
        response = client.get(url)
        if response.status_code == 200:
            print(f"URL {url} работает корректно.")
        else:
            print(f"URL {url} вернул ошибку {response.status_code}")

def check_templates():
    templates_to_check = [
        'analiz/task_list.html',
        'analiz/task_form.html',
    ]
    
    for template_name in templates_to_check:
        try:
            get_template(template_name)
            print(f"Шаблон {template_name} найден и корректен.")
        except TemplateDoesNotExist:
            print(f"Шаблон {template_name} не найден.")
        except Exception as e:
            print(f"Ошибка в шаблоне {template_name}: {e}")

# Запуск всех проверок
check_migrations()
check_tables()
check_urls()
check_templates()
