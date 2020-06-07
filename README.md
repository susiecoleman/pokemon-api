# Pokemon Search

API for searching for pokemon by either type or name. This is an API written in Python using the Flask framework. The API stores all available pokemon and can be queried to find pokemon that match a search criteria. A match is found if the query string is contained in either the type or name of the pokemon.

### Set up the API

Instructions are aimed at users of UNIX like systems

Requirements:

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [virtualenv](https://pypi.org/project/virtualenv/)

1. Create and activate Python virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

2. Install Requirements

```
pip install -r requirements.txt
```

### Run the API

Run:

```
flask run
```

The API will now be running on [`localhost:5000`](http://localhost:5000)

### Using the API

The API has two GET endpoints:

#### `/`

Test endpoint to check the API is running. Returns a 200 if the app is running.

Sample Request: `http://localhost:5000/`

#### `/pokemon`

This takes a parameter in the query string called `q` and returns a json object that contains a list all pokemon that contain q in either their type or name with type matches returned first.

Sample Request: `http://localhost:5000/pokemon?q="gr"`

Sample Response:

```
{
  "pokemon": [
    {
      "name": "Grookey",
      "type": "Grass"
    },
    {
      "name": "Thwackey",
      "type": "Grass"
    },
    {
      "name": "Rillaboom",
      "type": "Grass"
    },
    {
      "name": "Greedent",
      "type": "Normal"
    }
  ]
}
```
