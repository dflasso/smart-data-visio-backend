# Smart Data Visio Backend
Rest API with django, database mongoDB. The project implementes data analytics with panda, numpy, etc.

## Install Dependencys

### Versions

```
asgiref==3.4.1
Django==4.0
django-cors-headers==3.10.1
djangorestframework==3.13.1
djongo==1.3.6
dnspython==2.1.0
pymongo==3.12.1
pytz==2021.3
sqlparse==0.2.4
```

### Commants 

```
sudo apt-get install python3.9-venv 

cd <path_folder_project>

python3.9  -m venv .env 

cd <path_folder_project> 

source .env/bin/activate 

pip install django

//dependencias rest
pip install djangorestframework

pip install django-cors-headers

//driver mongoDB

pip install pymongo==3.12.1

pip install dnspython

```

## Get Started

```
python3.9 manage.py runserver
```

## Conexión mongoDB

1. get url conección for python. In this case mongo atlas give the url.

2. put the next setup

```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            "host": "mongodb+srv://<username>:<pass_word>@<host>/myFirstDatabase?retryWrites=true&w=majority",
            "name": "<databse_name>",
            "authMechanism":"SCRAM-SHA-1"
        }
    }
}

```
## Apps

### Security

#### Actualizar los modelos de seguridad en la base 

```
python3.9 manage.py makemigrations 
python3.9 manage.py migrate
```

Output
```
Operations to perform:
  Apply all migrations: Security, admin, auth, contenttypes, sessions
Running migrations:
This version of djongo does not support "NULL, NOT NULL column validation check" fully. Visit https://nesdis.github.io/djongo/support/
  Applying contenttypes.0001_initial...This version of djongo does not support "schema validation using CONSTRAINT" fully. Visit https://nesdis.github.io/djongo/support/
 OK
  Applying contenttypes.0002_remove_content_type_name...This version of djongo does not support "COLUMN DROP NOT NULL " fully. Visit https://nesdis.github.io/djongo/support/
This version of djongo does not support "DROP CASCADE" fully. Visit https://nesdis.github.io/djongo/support/
 OK
  Applying auth.0001_initial...This version of djongo does not support "schema validation using KEY" fully. Visit https://nesdis.github.io/djongo/support/
This version of djongo does not support "schema validation using REFERENCES" fully. Visit https://nesdis.github.io/djongo/support/
 OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying Security.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying sessions.0001_initial... OK
```

#### Crear un super usuario

ejecutar el comando 

```
python3.9 manage.py createsuperuser
```

Usuario creado
email: dany@gmail.com
dl.12345