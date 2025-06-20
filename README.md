# ETL_Python_SQL
Following along with the ETL in Python and SQL LinkedIn Learning course

## Chapter 1: What are ETLs?
Basic overview of ETLs and intro to Pandas

## Chapter 2: Extracting and Transforming Data with Python
More basic Pandas

## Chapter 3: Loading Data into Target Systems
Working with Python and the DB. ElephantDB is no longer supported so I created my own DB using MySQL Workbench.

## Chapter 4: Automating ETL Jobs: Scheduling ETL Jobs with Python
This chapter needs airflow installed. I installed it using a Docker container. Instructions in following section.

## Installing Apache Airflow
As mentioned above, I used a Docker container for this. Conda environments threw errors that I couldn't fix.

To start, I installed Docker Desktop at this [link](https://docs.docker.com/desktop/setup/install/windows-install/)

Once it was installed, I downloaded the `docker-compose.yaml` file from this [link](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#fetching-docker-compose-yaml). I then put this file in a new folder I created called `airflow_docker` located in `Users/myuser/Documents/`.

I then created a `.env` file in this same `airflow_docker` folder with the following code:
```
AIRFLOW_IMAGE_NAME=apache/airflow:3.0.0 
AIRFLOW_UID=50000
_PIP_ADDITIONAL_REQUIREMENTS=openpyxl
```

I then created a `requirements.txt` file in the same `airflow_docker` folder with the following code:
```
# requirements.txt
openpyxl
```

The last change I made was in `docker-compose.yaml`. In the `volumes` section, I added one line:
```
x-airflow-common:
  &airflow-common

  ...
  
  volumes:
    - ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
    - ${AIRFLOW_PROJ_DIR:-.}/logs:/opt/airflow/logs
    - ${AIRFLOW_PROJ_DIR:-.}/config:/opt/airflow/config
    - ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/plugins
    - ${AIRFLOW_PROJ_DIR:-.}/requirements.txt:/requirements.txt  # this line
```

After this, I was ready to run the container. I had errors running the container in the VSCode terminal, but running it in the base Windows terminal did not throw these errors. To run I used the command `docker compose up -d` (I have a new version of Docker Compose so I don't use a hyphen in between docker and compose, for older versions, use `docker-compose up -d`).

Once everything was running, I created a new user for login purposes. To do this, I ran the command `docker compose run airflow-worker airflow users create --role Admin --username admin --email admin@example.com --firstname firstname --lastname lastname --password admin`. This is an example, you can change the values of the username, password, etc. to your liking.

Once this was complete, I navigated to `localhost:8080`, logged in using my new credentials, and I could navigate around the Airflow GUI.

To close down the container, I ran `docker compose down`.
