# Usage

Change the folder permission to make sure that the container is able to access the directory:
```
$ sudo chmod -R 777 extra-addons
$ sudo chmod -R 777 etc
```

Start the container:
```
$ docker-compose up
```

* Then open `localhost:8099` to access Odoo 12.0. If you want to start the server with a different port, change **8099** to another value:

```
ports:
 - "8099:8069"
```

To run in detached mode, execute this command:

```
$ docker-compose up -d
```

# Custom addons

The **extra-addons** folder contains custom addons. 

# Odoo configuration

To change Odoo configuration, edit file: **etc/odoo.conf**.

# docker-compose.yml

* odoo:12.0
* postgres:9.5