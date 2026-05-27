# DaSSCo Storage Client

A simple client library used to call the DaSSco Storage API


### Installation

Requires Python 3.10+

```
python -m pip install dasscostorageclient 
```


### Getting started

```

Recommended to set env variables before usage. See env.example 

from dasscostorageclient import DaSSCoStorageClient

client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'

client = DaSSCoStorageClient(client_id, client_secret)

institutions = client.institutions.get()

```
### For testing/development.

```
Create .env as per env.example.
example.py can be run after .env has been created.

To run tests: 
pytest -s file.py