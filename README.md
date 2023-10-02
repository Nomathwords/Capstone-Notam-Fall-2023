# NOTAM

This is a capstone project for OU Fall 2023 CS.

# FRONTEND

Navigate to the frontend directory and run `npm install` to grab necessary packages from packages.json, then run `npm start`

# BACKEND

Before starting the backend, add a "credentials.py" file to the "airport" directory with these variables and the proper values in place:

```
client_id=""
client_secret=""
```

Airport Endpoint:

To hit the airport endpoint properly, open postman and add the following params to the parameter page:
![Alt text](image.png)

After doing so, the airport endpoint should return all the NOTAMS for that airport.
