# NOTAM

This is a capstone project for OU Fall 2023 CS.

# VERSIONS

Install the following, if not installed already:

1. python3: 3.8.10+ 
2. python django: 4.2.7
3. NPM: 9.8.1
4. Node: 18.18.0

# BACKEND ONLY

Before starting the backend, do the following steps:

1. Open a terminal inside the project file.
2. Add a "credentials.py" file to the "airport" directory with these variables and the proper values in place:

```
client_id=""
client_secret=""
```

3. Go to this link: https://adds-faa.opendata.arcgis.com/datasets/faa::airports-1/explore. Download the csv file of all the airports and move it to the "airport" directory.
4. Go to the "csv_parser.py" file and paste the file path to the "Airports.csv" file in the "airport_csv_path" at the top. Make sure to replace all "\" with "/".
5. Install the necessary django cors headers: `pip install django-cors-headers`

If you are running the backend only:
6.Open PostMan and paste in the folling endpoint: `http://127.0.0.1:8000/airport/?departure=OKC&destination=DFW`. This endpoing is using OKC as the departure and DFW as the destination. Feel free to change both of these.

7. Start the backend with the following command: `python3 manage.py runserver`.
8. Hit the send button and the program will begin execution.

# BACKEND AND FRONTEND

Before starting the backend, do the following steps:

1. Open a terminal inside the project file.
2. Add a "credentials.py" file to the "airport" directory with these variables and the proper values in place:

```
client_id=""
client_secret=""
```

3. Go to this link: https://adds-faa.opendata.arcgis.com/datasets/faa::airports-1/explore. Download the csv file of all the airports and move it to the "airport" directory.
4. Go to the "csv_parser.py" file and paste the file path to the "Airports.csv" file in the "airport_csv_path" at the top. Make sure to replace all "\" with "/".
5. Install the necessary django cors headers: `pip install django-cors-headers`
6. Start the backend with the following command: `python3 manage.py runserver`.

Before starting the frontend, do the following steps:

1. In a separate terminal, navigate to the frontend directory and run `npm install -f` to grab necessary packages from packages.json.
2. Once the installs finish, run `npm start`. A localhost window will open in your browser.
3. Input a departure and destination airport, such as `OKC` and `DFW`.
4. Click the run button, and after a few minutes, a list of sorted NOTAMs will appear in an accordian, which you can click to open and scroll through.
