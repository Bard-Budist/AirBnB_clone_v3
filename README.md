# AirBnB Clone - The Console - RESTful-API

![N|Solid](https://github.com/jdrestre/pictures-holberton-projects/blob/master/AirBnB_clone_v2_MySQL/hbnb_logo.png)

The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

===

## Description Project

### RESTful - Api Diaagram

![N|Solid](https://github.com/jdrestre/pictures-holberton-projects/blob/master/0x05AirBnBClone_RESTful-API/hbnb_step4%20diagram%20API.png)

---
Repository to study the following Topic: RESTful-API

### General

- What REST means
- What API means
- What CORS means
- What is an API
- What is a REST API
- What are other type of APIs
- Which is the HTTP method to retrieve resource(s)
- Which is the HTTP method to create a resource
- Which is the HTTP method to update resource
- Which is the HTTP method to delete resource
- How to request Rest API

## File Descriptions

[console.py](console.py) - the console contains the entry point of the command interpreter.
List of commands this console current supports:

- `EOF` - exits console
- `quit` - exits console
- `<emptyline>` - overwrites default emptyline method and does nothing
- `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the id
- `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
- `show` - Prints the string representation of an instance based on the class name and id.
- `all` - Prints all string representation of all instances based or not on the class name.
- `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

## Diagram Class

This diagram shows the relationship between all the classes created:

![N|Solid](https://github.com/jdrestre/pictures-holberton-projects/blob/master/AirBnB_clone_v2_MySQL/AirBnb_DB_diagrammclasses.jpg)

---

## How to start it

### FileStorage

The default mode.

In `FileStorage` mode, every time the backend is initialized, HolbertonBnB
instantiates an instance of `FileStorage` called `storage`. The `storage`
object is loaded/re-loaded from any class instances stored in the JSON file
`file.json`. As class instances are created, updated, or deleted, the
`storage` object is used to register corresponding changes in the `file.json`.

### DBStorage

Run by setting the environmental variables `HBNB_TYPE_STORAGE=db`.

In `DBStorage` mode, every time the backend is initialized, HolbertonBnB
instantiates an instance of `DBStorage` called `storage`. The `storage` object
is loaded/re-loaded from the MySQL database specified in the environmental variable
`HBNB_MYSQL_DB`, using the user `HBNB_MYSQL_USER`, password `HBNB_MYSQL_PWD`, and
host `HBNB_MYSQL_HOST`. As class instances are created, updated, or deleted, the
`storage` object is used to register changes in the corresponding MySQL database.
Connection and querying is achieved using SQLAlchemy.

Note that the databases specified for `DBStorage` to connect to must already be
defined on the MySQL server. This repository includes scripts
[setup_mysql_dev.sql](./setup_mysql_dev.sql) and [setup_mysql_test.sql](./setup_mysql_test.sql)
to set up `hbnb_dev_db` and `hbnb_test_db` databases in a MySQL server,
respectively.

### Console

The console is a command line interpreter that permits management of the backend
of HolbertonBnB. It can be used to handle and manipulate all classes utilized by
the application (achieved by calls on the `storage` object defined above).

---

## How to use it

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution of the file `console.py` at the command line.

``` python
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the file `console.py` by itself:

``` python
./console.py
```

While running in interactive mode, the console displays a prompt for input:

``` python
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

``` python
$ ./console.py
(hbnb) quit
$
```

```python
$ ./console.py
(hbnb) EOF
$
```

---

## Examples

The HolbertonBnB console supports the following commands:

### create

- Usage: `create <class> <param 1 name>=<param 1 value> <param 2 name>=<param 2 value> ...`

``` python
$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb)
(hbnb) create State name="California"
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T2
1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}, {'id': 'd80e0344-63eb-43
4a-b1e0-07783522124e', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7,
842160), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name
': 'California'}}
```

### show

- Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

``` python
$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828),
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)
(hbnb) User.show(1e32232d-5a63-4d92-8092-ac3240b29f46)
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828),
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)
```

#### all

- Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```python
$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb) create User
b742dbc3-f4bf-425e-b1d4-165f52c6ff81
(hbnb) create User
8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
(2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
(hbnb) User.all()
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User]
(b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2
, 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44,
15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
(hbnb)
(hbnb) all
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
del] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(20
19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21,
45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 2
1, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 97
4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 4
3, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348
), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
```

---

## Testing :straight_ruler

Command used for unittest:

```python
$python3 unittest -m discover tests
```

Or you can specify a single test file:

```python
$python3 unittest -m tests/test_console.py
```

## Task Project

---
File Name|Task Name|Task Description
---|---|---
[**`AirBnB_clone_v3`**](https://github.com/Bard-Budist/AirBnB_clone_v3)|**0. Restart from scratch!**|Repository cloned.
[**`AirBnB_clone_v3`**](https://github.com/Bard-Budist/AirBnB_clone_v3)|**1. Never fail!**|python3 -m unittest discover tests.
[**`code_review.txt`**](https://github.com/Bard-Budist/AirBnB_clone_v3/blob/master/code_review.txt)|**2. Code review**|For this project, you will need to review a peer’s pull request on the branch storage_get_count (which will be made for question 3), and then accept the pull request, with your review in the comments.
[**`models/engine/db_storage.py`**](https://github.com/Bard-Budist/AirBnB_clone_v3/blob/master/models/engine/db_storage.py), [**`models/engine/file_storage.py`**](https://github.com/Bard-Budist/AirBnB_clone_v3/blob/master/models/engine/file_storage.py), [**`tests/test_models/test_engine/test_db_storage.py`**](https://github.com/Bard-Budist/AirBnB_clone_v3/blob/master/tests/test_models/test_engine/test_db_storage.py), [**`tests/test_models/test_engine/test_file_storage.py`**](https://github.com/Bard-Budist/AirBnB_clone_v3/blob/master/tests/test_models/test_engine/test_file_storage.py)|**3. Improve storage**|Update DBStorage and FileStorage, adding two new methods. All changes should be done in the branch storage_get_count

## Author

---

- Juan David Restrepo Z. [@jdrestre](https://twitter.com/jdrestre)
- Giovanny Pérez [@Giovanni_Perez1](https://twitter.com/Giovanni_Perez1)
- Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)
- Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)

---
![Logo Holberton](https://www.holbertonschool.com/holberton-logo.png) ![Sea Horse Icon](https://intranet.hbtn.io/assets/holberton-logo-coral-27055cb2f875eb10bf3b3942e52a24581bc0667695bdc856d4f08b469b678000.png)
