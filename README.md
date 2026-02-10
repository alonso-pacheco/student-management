# Student CRUD
In this repository is the backend and frontend of project

## Run project with Docker
1. Activate Docker
2. In Backend project, copy `.env.example` file and change name to `.env` and update MySQL connection string
3. In Frontend project, copy `.env.example` file and change name to `.env` and update endpoint

2. Run `docker compose up`

## Run project by folder
1. Access to folder project
2. Activate virtual environment
    * Windows: venv\Scripts\activate
    * Linux: source venv\bin\activate
3. In Backend project, copy .env.example file and change name to `.env` and update MySQL connection string
4. Install dependencies
``` bash
pip install poetry
poetry install
```
5. To run backend app use command
``` bash
flask --app app run
or
flask run
```
6. To run frontend app use command
``` bash
python manage.py runserver
```




### Changes
1. Modify `builkit` to Docker in Windows. In the path Docker app > Settings > Docker engine > builkit in False
