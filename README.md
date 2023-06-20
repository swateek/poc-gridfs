## POC - MongoDB GridFS

A working model for Python with Mongo's GridFS framework.

### The Development Setup

1. Create a virtual environment and install dependecies

```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r pip-requirements.txt --no-cache-dir
```

2. Download and Install MongoDB Docker

```bash
    docker pull mongo
    docker run -tid --rm --name dev-mongo -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=admin mongo
```

3. To be able to browse MongoDB collections, download [Studio 3T](https://studio3t.com/download-studio3t-free/)

```text
    connection name: dev-mongo
    IP: localhost
    port: 27017
    Authentication:
        mode: basic
        username: admin
        password: admin
```

4. Download sample .wav files from this [link](https://file-examples.com/index.php/sample-audio-files/sample-wav-download/) and put these files in a folder named **input**

```bash
    wget https://file-examples.com/wp-content/storage/2017/11/file_example_WAV_1MG.wav
    wget https://file-examples.com/wp-content/storage/2017/11/file_example_WAV_2MG.wav
    wget https://file-examples.com/wp-content/storage/2017/11/file_example_WAV_5MG.wav
    wget https://file-examples.com/wp-content/storage/2017/11/file_example_WAV_10MG.wav
```

### Using MongoDB Docker

```bash
    docker exec -ti dev-mongo bash
    mongosh
    use admin
    db.auth("admin", "admin");
    show dbs


    db.createCollection("mysample");
    show collections;
```
