# Guardians - PolyHx2022

![original](https://user-images.githubusercontent.com/27878892/153782716-3d3a13cb-da1c-45c3-b0f8-b13fbfa8679d.png)

You can consult our [Devpost submission](https://devpost.com/software/guardians-12iszg) to learn more about our project and see a demo.

## Technology Stack

- VueJs
- Flask
- SQLite
- BootstrapVue
- Google Maps
- Assembly AI
- Twillio SMS

## Backend

To run the Flask backend, you need to navigate to the Backend folder, start a venv and install the requirements:

``pip install -r requirements.txt``

The SQLite database needs to be created and seeded, therefore you need to run the SQL scripts in `schema.sql` and `tablePopulation.sql` in a local MySQL database.

Once dependencies are installed, you can run the backend server using the following command:

``export FLASK_APP=main``

``flask run``

It should be accessible at `localhost:5000`

To utilize the external services used in this application, you will need to create a copy of `config.yml` from `config.template.yml` and insert the required API keys.

## Frontend

To run the Vue frontend, you need to navigate to the `frontend` directory and install dependencies first:

``npm install``

Once dependencies are installed, you can run the server using the following command:

``npm run serve``

It should be accessible at `localhost:8080`

To utilize the external services used in this application, you will need to create `env.local` from `env.example` and insert the required API keys.
