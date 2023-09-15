# PGVector Demo
Showcase how to implement a vectorized search using PostgreSQL and Python.

## 🧰 Features
- Docker-compose setup for PostgreSQL with pgvector extension
- Python code to insert data into the database
- Python code to create a vectorized search using pgvector

## 💻 Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:
    ```shell
    pip install -r requirements.txt
    ```
3. Run the following command to set up the database (you have Docker installed, right?)
    ```shell
    docker-compose up -d
    ```
4. Run the script `add_test_data.py` to insert some data into the database:
5. Run the script `test_search.py` to test a vectorized search.
