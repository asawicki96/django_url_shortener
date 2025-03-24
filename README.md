# url_shortener
URL shortener

**Installation:**

Python version is specified in .python-version file.

1. Being in url_shortener directory run:
virtualenv venv 

2. Activate venv and run:
pip install -r requirements.txt

3. Run migrations by executing command:
python manage.py migrate


**Running tests:**
1. Execute command:
pytest

**Running dev server:**
1. Execute command:
python manage.py runserver

Useful links:
- swagger docs: localhost:8000/docs


**How to extract long url from generated short_url?**
1. Send GET request to the /short_url/ attaching it's alias at the end of url.

**Justifications:**
1. Snowflake ID generation - allows to generate globally unique IDs in distributed systems.
It makes API servers more scalable.
2. Short ulrs aliases should be indexed aswell as long urls because of data access patterns
(checking if alias exist for given long url, fetching the long url for given alias)

**Areas of potential improvements:**
1. Sharded database -> To take full advantage from generating globally unique SnowFlake IDs
we should store the generated short urls in sharded database (e.g MongoDB or DynamoDB). 
Therefore we would be able to scale the database aswell as API servers.
It would require using some abstraction like Repository pattern to handle data access
or incorporating some tools like ODM (Object Document Mapper).
For the purpose of this showcase I used relational DB which can be scaled only vertically 
but is easy to setup in dev environment (sqlite) and is supported by DRF out of the box. 
The decision whether we need sharded DB should be driven by the estimated QPS (Query Per Second) and
by the estimated storage needs (for example after answering the question "How many URLs will be generated daily).

2. Adding caching to prevent hitting database on each request (
    because we are checking whether the alias for given long_url exists already
).
3. Use some package managers like poetry/uv.
4. Use code static analysis tools like flake8, ruff.
