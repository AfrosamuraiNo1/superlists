
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
## 2.В вкладке выбрать VPS.
![](https://github.com/AfrosamuraiNo1/superlists/blob/master/foto_readme/photo_2023-03-19_09-28-12.jpg)
## 3.На странице заказываем base1 (самый простой сервер).
![](https://github.com/AfrosamuraiNo1/superlists/blob/master/foto_readme/photo_2023-03-19_09-28-06.jpg)
## 3.Делаем как на фото и заказываем сервер.
![](## 3.На странице заказываем base1 (самый простой сервер).
![](https://github.com/AfrosamuraiNo1/superlists/blob/master/foto_readme/photo_2023-03-19_09-26-20.jpg)

## Generate an SSH key

If you've never created one before, the command is

```bash
ssh-keygen
```

**NOTE** *If you're on Windows, you need to be using Git-Bash for `ssh-keygen`
and `ssh` to work. There's more info in the
[installation instructions chapter](http://www.obeythetestinggoat.com/book/pre-requisite-installations.html)*

Just accept all the defaults if you really want to just get started in a hurry,
and no passphrase.

Later on, you'll want to re-create a key with a passphrase for extra security,
but that means you have to figure out how to save that passphrase in such a way
that Fabric won't ask for it later, and I don't have time to write instructions
for that now!

Make a note of your "public key"

```bash
cat ~/.ssh/id_rsa.pub
```

More info on public key authentication [here](https://www.linode.com/docs/networking/ssh/use-public-key-authentication-with-ssh/)
and [here](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-digitalocean-droplets)


## Start a Droplet

A "droplet" is Digital Ocean's name for a server.  Pick the default Ubuntu,
the cheapest type, and whichever region is closest to you. You won't need
access to the ancillary services that are available (Block storage, a VPC
network, IPv6, User-Data, Monitoring or Back-Ups)

* Choose **New SSH Key** and upload your public key from above

Make a note of your server's IP address once it's started


## Log in for the first time


```bash
ssh root@your-server-ip-address-here
```

It should just magically find your SSH key and log you in without any
need for a password.


## Create a non-root user

```bash
useradd -m -s /bin/bash elspeth # add user named elspeth 
# -m creates a home folder, -s sets elspeth to use bash by default
usermod -a -G sudo elspeth # add elspeth to the sudoers group
passwd elspeth # set password for elspeth
su - elspeth # switch-user to being elspeth!
```


## Add your public key to the non-root user as well.

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

Now verify you can SSH in as elspeth from your laptop


```bash
ssh elspeth@your-server-ip-address-here
```

Also check you can use "sudo" as elspeth

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
