## AirBnB_clone Project

This project under the guidance of `alxswe` is the first step towards my full web application: the AirBnB clone. This first step is of importance because we'll be using what was built here for other following projects: HTML/CSS templating, database storage, API, front-end integration…
In this project, the storage type we'll be using is a file storage type (written in JSON) for its ubiquity in many languages.

Each task is linked and will help us to:

-    put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
-    create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-    create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
-    create the first abstracted storage engine of the project: File storage.
-    create all unittests to validate all our classes and storage engine


[AUTHORS](AUTHORS)                  The Authors that Contribute to success of the Project
[The Console](console.py)           The Command line Interpreter. Used to retrieve, manipulate, query etc the models. More information is given below
[Base Model](models/base_model.py)  The Parent Class where all other models inherits from. It takes of the the initialization, serialization and deserialization of instances
[City Model](models/city.py)        Contains the State name and State ID of a User
[Place Model](models/place.py)      contains name, user_id, city_id, description etc needed to know about where a user is
[Review Model](models/review.py)    contains the place_id, user_id and arbitrary text
[State Model](models/state.py)      contains the State where a user is
[User Model](models/user.py)        contains first name, last name, email and password of a user
[File Storage](models/engine/file_storage.py)   This is responsible for saving any new instances created into a file (file storage type). It also takes the function of loading previously created instances for them to be accessed.

### The Console
`The Console` is command line interpreter used to query, retrieve and manipulate data.
You can simply start the interpreter by running the executable file `./console.py`. This will display a terminal with a "(hbnb) " prompt.

##### Some of the functions that can be done on the `Console` include:

* `?` or `help`: list available `commands` in the `Console`. Also provides information about a `command`
    `Usage`:    `help`
                `?`
                `help` cmd
                `?` cmd
    `examples`: help, ? create, help count

* `all`: Prints all or a given class existing instance;
    `Usage`:    `all`
                `all()`
                `all` <class name>
                `all()` <class name()>
                `all` <class name()>
                `all()` <class name>
                <class name>.`all()`
                <class name>.`all`
    `examples`: all, all BaseModel, User.all(), Place.all

* `count`: counts the number of a given instance present;
    `Usage`:    `count` <class name>
                `count()` <class name()>
                `count` <class name()>
                `count()` <class name>
                <class name>.`count()`
                <class name>.`count`
    `examples`: count Review, count() Amenity, User.count(), City.count

* `create`: Creates an instance;
    `Usage`:    `create` <class name>
                `create` <class name()>
                `create()` <class name>
                `create()` <class name()>
                <class name>.`create()`
                <class name>.`create`
    `examples`: create State, Review.create(), create() City

* `destroy`: Destroys an instance;
    `Usage`:    `destroy` <class name> <id>
                `destroy` <class name()> <id>
                `destroy()` <class name> <id>
                `destroy()` <class name()> <id>
                <class name>.destroy(<id>)
    `examples`: destroy Amenity 1234-5678-efse, BaseModel.destroy(8343-sefe-2343)

* `show`: Shows an instance;
    `Usage`:    `show` <class name> <id>
                `show()` <class name()> <id>
                `show` <class name()> <id>
                `show()` <class name> <id>
                <class name>.`show(<id>)`
    `examples`: show BaseModel, show() State, User.count(), Place.count

* `update`: Update an existing instance;
    `Usage`:    `update` <class name> <id> <attribute name> "<attribute value>"
                `update` <class name()> <id> <attribute name> "<attribute value>"
                `update()` <class name()> <id> <attribute name> "<attribute value>"
                `update()` <class name> <id> <attribute name> "<attribute value>"
                <class name>.`update`(<id>, <attribute name>, "<attribute value>")
                <class name>.`update`(<id>, <{"atrr1": "val1", "attr2": val2}>)
    `examples`: update User 34343-2343-eser attribute_name "attribute_value",
                State.update(3234-24dfe-eerd, attribute_name, "attribute_value")
                City.update(dfeif-were-3433, {"attr1": "val1", "attr2": "val2"})

* `Ctrl + D`: Sends terminating signal to exit the `Console`

* `quit`: Quits the `Console`
    `Usage`: `quit`


###### NOTE:
The Available Classes are: `Amenity`, `BaseModel`, `City`, `Place`, `Review`, `State`, `User`
