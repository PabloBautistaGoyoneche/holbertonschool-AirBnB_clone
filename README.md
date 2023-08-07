## AirBnB CLONE CONSOLE
`holbertonschool-AirBnB_clone project`

[![65f4a1dd9c51265f49d0.png](https://i.postimg.cc/RFYVF6GW/65f4a1dd9c51265f49d0.png)](https://postimg.cc/5YwMKthJ)

<h2>Description</h2>

This is the first part of the AirBnB Clone project for Holberton: The objective of this project is to implement a server, with a simple copy of the AirBnB web application to demonstrate the understanding and development of front-end and back-end technical skills.

<h2>The Command Interpreter</h2>

Create a command line interpreter to manipulate data without a visual interface.

The first thing is to manipulate the storage system. This will give us an abstraction of our objects, how they are stored and how they are persisted, via JSON files, which means we don't have to look at how our objects are stored. This abstraction will also allow us to change the storage type easily without updating our entire database.

The console will be used to validate that this storage engine is working properly.

<h2>How to Start Using This?</h2>


To start using the interpreter, write one of these lines of code:

<h3>Interactive Mode</h3>

`User$ ./console.py`

<h3>Non-interactive Mode</h3>

` User$ "user command" | ./console.py`

<h2>All the Commands You Can Use</h2>


- `quit` - Use it to exit the console, only in interactive mode
- `create` - Creates an instance - Needs: Class - Usage: create Class
- `show` - Prints the string representation of an instance - Needs: Class and id - Usage: show specific Class with ID
- `destroy` - Deletes an intance - Use: Class and id - Usage: destroy specific Class with ID
- `all` - Prints all string representation of all instance - Needs: Opcional (Class) - Usage: show all or all of a specific class
- `update` - Updates an instance - Use: Class, id, attribute and value for the attribute - Usage: update value attribute of specific Class with ID
  
</p>

</details>

<details><summary> Examples </summary>

<p>


<h2>"create" Examples</h2>

```
(hbnb) create BaseModel
60d4e689-a246-405b-9d42-88428f99a105
(hbnb) create BaseModel
09de3adc-993d-44c0-8a7a-f62c62e8e870
(hbnb) create User
9dc47629-ad61-442d-8865-c82aedfa0ee5
(hbnb) create Place
d7820d61-423c-44e3-aa7b-0018ca8c66a8
(hbnb) create aleatory
** class doesn't exist **
(hbnb) create
** class name missing **
```

<h2>"Show" Examples</h2>

```
(hbnb) show BaseModel 09de3adc-993d-44c0-8a7a-f62c62e8e870
[BaseModel] (09de3adc-993d-44c0-8a7a-f62c62e8e870) {'id': '09de3adc-993d-44c0-8a7a-f62c62e8e870', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 40, 440464), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 40, 440474)}
(hbnb) show BaseModel 60d4e689-a246-405b-9d42-88428f99a105
[BaseModel] (60d4e689-a246-405b-9d42-88428f99a105) {'id': '60d4e689-a246-405b-9d42-88428f99a105', 'created_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826499), 'updated_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826512)}
(hbnb) show BaseModel aleatory
** no instance found **
(hbnb) show BaseModel 
** instance id missing **
(hbnb) show aleatory
** class doesn't exist **
(hbnb) show 
** class name missing **
```

<h2>"Destroy" Examples</h2>

```
(hbnb) destroy BaseModel 09de3adc-993d-44c0-8a7a-f62c62e8e870
(hbnb) show BaseModel 09de3adc-993d-44c0-8a7a-f62c62e8e870
** no instance found **
(hbnb) destroy BaseModel aleatory
** no instance found **
(hbnb) destroy BaseModel 
** instance id missing **
(hbnb) destroy aleatory
** class doesn't exist **
(hbnb) destroy 
** class name missing **
```

<h2> "All" Examples</h2> 

```
(hbnb) all BaseModel
["[BaseModel] (60d4e689-a246-405b-9d42-88428f99a105) {'id': '60d4e689-a246-405b-9d42-88428f99a105', 'created_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826499), 'updated_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826512)}"]
(hbnb) all User
["[User] (9dc47629-ad61-442d-8865-c82aedfa0ee5) {'id': '9dc47629-ad61-442d-8865-c82aedfa0ee5', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 52, 306321), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 52, 306330)}"]
(hbnb) all Place
["[Place] (d7820d61-423c-44e3-aa7b-0018ca8c66a8) {'id': 'd7820d61-423c-44e3-aa7b-0018ca8c66a8', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257449), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257458)}"]
(hbnb) all aleatory
** class doesn't exist **
(hbnb) all
["[BaseModel] (60d4e689-a246-405b-9d42-88428f99a105) {'id': '60d4e689-a246-405b-9d42-88428f99a105', 'created_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826499), 'updated_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826512)}", "[User] (9dc47629-ad61-442d-8865-c82aedfa0ee5) {'id': '9dc47629-ad61-442d-8865-c82aedfa0ee5', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 52, 306321), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 52, 306330)}", "[Place] (d7820d61-423c-44e3-aa7b-0018ca8c66a8) {'id': 'd7820d61-423c-44e3-aa7b-0018ca8c66a8', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257449), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257458)}"]
```

<h2>"Update" Examples </h2>

```
(hbnb) show Place d7820d61-423c-44e3-aa7b-0018ca8c66a8
[Place] (d7820d61-423c-44e3-aa7b-0018ca8c66a8) {'id': 'd7820d61-423c-44e3-aa7b-0018ca8c66a8', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257449), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257458)}
(hbnb) update Place d7820d61-423c-44e3-aa7b-0018ca8c66a8 number_rooms 3
(hbnb) show Place d7820d61-423c-44e3-aa7b-0018ca8c66a8
[Place] (d7820d61-423c-44e3-aa7b-0018ca8c66a8) {'id': 'd7820d61-423c-44e3-aa7b-0018ca8c66a8', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257449), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257458), 'number_rooms': '3'}
(hbnb) update Place d7820d61-423c-44e3-aa7b-0018ca8c66a8 number_rooms 
** value missing **
(hbnb) update Place d7820d61-423c-44e3-aa7b-0018ca8c66a8
** attribute name missing **
(hbnb) update Place aleatory
** no instance found **
(hbnb) update Place 
** instance id missing **
(hbnb) update aleatory
** class doesn't exist **
(hbnb) update 
** class name missing **
```

<h2>"Quit" Examples </h2>

```
(hbnb) quit
User$ 
```

</details>

</p>

</details>

|COLLABORATORS|
-------------------------------------------------------------------------
| Alexander Rivera Del Valle |  Pablo Bautista Goyoneche |
