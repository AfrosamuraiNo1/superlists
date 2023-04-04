from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random, os



REPO_URL = 'https://github.com/AfrosamuraiNo1/superlists' #Может потребоваться обновить переменную REPO_URL, используя
                                                      #URL-адрес вашего репозитория Git на его сайте обмена исходным кодом.

def deploy():
    '''развернуть'''
    
    site_folder = f'/home/{env.user}/sites/{env.host}' #env.host будет содержать адрес сервера, который мы указали в командной строке, например superlists.ottg.eu.
                                                       #env.user будет содержать имя пользователя, которое вы используете для входа на сервер.    
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)#env.user будет содержать имя пользователя, которое вы используете для входа на сервер.
    _update_env(source_folder)
    _update_static_files(source_folder, site_folder)
    _update_database(source_folder, site_folder)

def _create_directory_structure_if_necessary(site_folder): #Cоздает папки внутри общего каталога 'database', 'static', 'virtualenv', 'source'
    '''создать структуру каталога, если нужно'''
    for subfolder in ('database', 'static', 'env', 'source'):
        run(f'mkdir -p {site_folder}/{subfolder}')

def _get_latest_source(source_folder): #Проверяем наличие папки гит если нет копируем с github если есть обновляем.
    '''получить самый свежий исходный код'''
    if exists(source_folder + '/.git'):
        run(f'cd {source_folder} && git fetch')
    else:
        run(f'git clone {REPO_URL} {source_folder}')
        current_commit = local('git log -n 1 --format=%H', capture=True)
        run(f'cd {source_folder} && git reset --hard {current_commit}') #??? Нужен  ли ресет

def _update_settings(source_folder, site_name):#В фаиле settings.py меняем значения и создаем новый секретный ключ
    '''обновить настройки'''
    settings_path = source_folder + '/superlists/superlists/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path, 'ALLOWED_HOSTS =.+$', f'ALLOWED_HOSTS = ["{site_name}"]')
    secret_key_file = source_folder + '/superlists/superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_env(source_folder):#Обновляем виртуальное окружение
    '''обновить виртуальную среду'''
    env_folder = source_folder + '/../env'
    if not exists(env_folder + '/bin/pip'):
        run(f'python3.10 -m venv {env_folder}')
    run(f'{env_folder}/bin/pip install -r {source_folder}/requirements.txt')

def _update_static_files(source_folder,site_folder):
    '''обновить статические файлы'''
    run(f'cd {source_folder}/superlists' 
        f' && {site_folder}/env/bin/python manage.py collectstatic --noinput')
    
def _update_database(source_folder, site_folder):
    '''обновить базу данных'''
    run(f'cd {source_folder}/superlists'
    f' && {site_folder}/env/bin/python manage.py migrate --noinput')