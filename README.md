# Stori Tech Challenge

It is Stori's chanllege as part of its intervias process. It was developed by Miguel Perdigón using Python 3.8 language and Psotgres database. The program loads the data coming from the transactions.cvs file into the database and then processes it to make a summary report that arrives in the mail.

## Table of Contents

1. [Configuration](#configuration)
2. [Use](#use)

## Configuration
The first thing to do is to set the environment variables that are defined in the docker-compose

- POSTGRES_USER: it is optional to modify it, you can leave it as it is by default, but if you change it, it must be the same in both db and app.
- POSTGRES_PASSWORD: it is optional to modify it, you can leave it as it is by default, but if you change it, it must be the same in both db and app.
- GMAIL_PASSWORD: contact the developer for the password miguelperdigon91@gmail.com
- EMAIL_TARGET: is the e-mail address where you will receive the result of the program execution.

## Use
Once the environment variables have been configured, you must open a terminal and move the current file to the program folder and then execute the following docker command 
```
sudo docker-compose up
```

To view the records that are stored in the database go to the browser and enter the following in the browser
```commandline
http://localhost:5050/browser/
```
The username and password are defined in the environment variables PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD

Once inside, you create a new connection to a database, which must be called as defined in POSTGRES_DB. the host you put 'db' and complete the other fields with whatever is defined in the environment variables POSTGRES_USER and POSTGRES_PASSWORD.
