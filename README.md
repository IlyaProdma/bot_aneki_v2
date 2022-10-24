To start the db service type in `docker-compose up` (you may also use `-d` flag to start in detached mode)
to start the bot service type in `python bot.py`

you need to set up a .env file with the following variables:
- *DBNAME* - your database name
- *DBUSER* - your database user name
- *DBPASSWORD* - your database user password
- *HOST* - your database server host
- *PORT* - your database server port
- *TOKEN* - your TG-bot token