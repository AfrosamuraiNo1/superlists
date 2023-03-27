Обеспечение работы нового сайта
================================
## Необходимые пакеты:
* nginx
* Python 3.10
* virtualenv + pip
* Git
например, в Ubuntu:
sudo apt-get install nginx git python3.10 python3.10-venv
## Конфигурация виртуального узла Nginx
* см. nginx.template.conf
* заменить SITENAME, например, на staging.my-domain.com
## Служба Systemd
* см. gunicorn-systemd.template.service
* заменить SITENAME, например, на staging.my-domain.com
## Структура папок:
Если допустить, что есть учетная запись пользователя в /home/username
/home/username
└── sites
└── SITENAME
├── database
├── source
├── static
└── virtualenv