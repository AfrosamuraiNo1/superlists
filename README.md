
## Test-Driven Development with Python. 

Obey the Testing Goat: Using Django, Selenium, and JavaScript


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/Made-Django4.1.6-<COLOR>.svg)](https://shields.io/)


# Ультракороткие инструкции о том, как получить Linux-сервер

Эти инструкции предназначены в качестве дополнения к
[глава о развертывании моей книги](http://www.obeythetestinggoat.com/book/chapter_manual_deployment.html ).


## Используй www.reg.ru

Я переписал инструкцию используя другую платформу [REG.ru](https://www.reg.ru/domain/new/?rlink=reflink-11142889 ). 
Выбрал этот сервис так как я сним заочно знаком и мне он показался простым и не кусачим по цифрам, вот [моя реферальная ссылка](https://www.reg.ru/domain/new/?rlink=reflink-11142889 ) Мне будет приятно если вы зарегистрируетесь по ней, таким образом поможете моему проекту. Так же можете воспользоваться моей скидкой 5% на nokynky B4D0-C80D-D436-581B (Промо код).

## 1.На странице выбрать VPS.
![](https://github.com/AfrosamuraiNo1/superlists/blob/master/foto_readme/photo_2023-03-19_09-28-17.jpg)
## 2.В вкладке выбрать VPS на Linux.
![](https://github.com/AfrosamuraiNo1/superlists/blob/master/foto_readme/photo_2023-03-19_09-28-12.jpg)
## 3.На странице заказываем base1 (самый простой сервер).
![](https://github.com/AfrosamuraiNo1/superlists/blob/master/foto_readme/photo_2023-03-19_09-28-06.jpg)
## 4.Делаем как на фото и заказываем сервер.
![](https://github.com/AfrosamuraiNo1/superlists/blob/master/foto_readme/photo_2023-03-19_09-26-20.jpg)

## Создать ключ SSH.

Создайте ключ в командной строке.

```bash
ssh-keygen
```

Скопируйте ваш "public key"

```bash
cat ~/.ssh/id_rsa.pub
```
## Подключение к виртуальному серверу.

```bash
ssh root@your-server-ip-address-here (ssh root@123.123.123.123)
```

## Создать пользователя без прав root.

```bash
useradd -m -s /bin/bash elspeth # Создать пользователя с именем elspeth 
# -m созадает в домашней папке имя
# -s Пользователь elspeth может пользоваться командами в командной строке не как администратор

usermod -a -G sudo elspeth # Добавить elspeth в группу выполнения команд sudo
passwd elspeth # Пароль elspeth

su - elspeth # Начать пользоваться аккаунтом elspeth!
```


## Добавим публичный ключ для пользователя elspeth.

* Copy your public key to your clipboard, and then


```bash
# as user elspeth
mkdir -p ~/.ssh
echo 'PASTE
YOUR
PUBLIC
KEY
HERE' >> ~/.ssh/authorized_keys
```

Теперь можно напрямую заходить под от пользователя elspeth.


```bash
ssh elspeth@your-server-ip-address-here (ssh root@123.123.123.123)
```

Проверьте можете ли вы использовать комманду "sudo" пользователем elspeth. 

```bash
sudo echo hi
```


## Map your domains to the server

There's one more thing you need to do in the book, which
is to map a domain name to your server's IP address.

If you don't already own a domain name you can use (you don't
have to use the *www.* subdomain, you could use *superlists.yourdomain.com*),
then you'll need to get on from a "domain registrar".  There are loads
out there, I quite like Gandi or the slightly-more-friendly (but
no 2FA) 123-reg.

If you want a free one there's [dot.tk](http://www.dot.tk).  Be aware
that their business model is based on ads, so there will be ads
all over your domain until you configure it.

Once you have a domain, you need to set up a couple of **A-records** in
its DNS configuration, one for your "staging" subdomain and one for your
"live" subdomain.  Mine are *superlists.ottg.eu* and *superlists-staging.ottg.eu*
for example.

*(tip: DNS changes take time to propagate, so if your domain doesn't
take you to the server straight away, you may need to wait.  Some registrars
will let you control this using a setting called "TTL")*.


And now you should be all set to follow the rest of the instructions in 
the manual deployment chapter


# Pull requests and suggestions accepted!

I literally threw these instructions together in 10 minutes flat, so I'm 
sure they could do with improvements.  Please send in suggestions, typos,
fixes, any common "gotchas" you ran into that you think I should mention.

