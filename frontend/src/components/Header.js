import React, { useEffect } from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import { Typography } from "@mui/material";
import { makeStyles } from "@mui/styles";
import Box from "@mui/material/Box";
import logo from "../assets/plane.svg";
import Grid from "@mui/material/Grid";
import AirportFilter from "./AirportFilter";
import { useState } from "react";
import Alert from "@mui/material/Alert";
import CustomizedAccordian from "./CustomizedAccordian";
import CircularProgress from "@mui/material/CircularProgress";

const useStyles = makeStyles((theme) => ({
  toolBarMargin: {
    ...theme.mixins.toolbar,
  },
  logo: {
    height: "6em",
  },
}));

export default function Header(props) {
  const classes = useStyles();

  const [departureAirport, setDepartureAirport] = useState(null);
  const [arrivalAirport, setArrivalAirport] = useState(null);
  const [error, setError] = useState(false);
  const [submitClicked, setSubmitClicked] = useState(false);

  const [submit, setSubmit] = useState(false);

  // Load notams from json

  const [notams, setNotams] = useState(null);

  useEffect(() => {
    console.log(notams);
    if (notams !== null) {
      setSubmit(true);
      console.log(notams);
    }
  }, [notams]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setSubmitClicked(true);

    // Set up backend call here
    if (
      departureAirport &&
      arrivalAirport &&
      departureAirport !== arrivalAirport
    ) {
      // http://127.0.0.1:8000/airport/?departure=OKC&destination=LAW
      // fetch data from a url endpoint
      try {
        const res = await fetch(
          `http://127.0.0.1:8000/airport/?departure=${departureAirport.identifier}&destination=${arrivalAirport.identifier}`
        );
        const data = await res.json();
        // if history not [] set history to data
        if (data.length !== 0) {
          setNotams(data);
        }
      } catch (error) {
        console.log(error);
      }
      setError(false);
    } else {
      setError(true);
    }
  };

  const handleCloseAlert = () => {
    setError(false);
  };

  return (
    <React.Fragment>
      <AppBar position="fixed" color="primary">
        <Toolbar
          disableGutters
          sx={{
            gap: "19em",
          }}
        >
          <img src={logo} alt="plane logo" className={classes.logo} />
          <Typography color="secondary" variant="h3">
            Enter Flight Information
          </Typography>
        </Toolbar>
        {error ? (
          <div
            style={{
              display: "flex",
              flexDirection: "row",
              width: "100%",
              zIndex: "100",
              alignContent: "center",
              justifyContent: "space-between",
            }}
          >
            <Alert
              severity="info"
              style={{
                width: "100%",
                justifyContent: "center",
                fontSize: 16,
                borderRadius: "0px",
              }}
            >
              Please enter both departure and arrival airports!
            </Alert>
            <div
              style={{
                backgroundColor: "#E8F5FC",
                justifyContent: "center",
                alignContent: "center",
                display: "flex",
                padding: "10px 10px",
              }}
            >
              <button
                style={{
                  color: "indianred",
                  backgroundColor: "transparent",
                  border: "1px solid grey",
                  cursor: "pointer",
                  borderRadius: "5px",
                  padding: "8px 10px",
                  fontSize: "14px",
                }}
                onClick={handleCloseAlert}
              >
                X
              </button>
            </div>
          </div>
        ) : null}
      </AppBar>
      <div className={classes.toolBarMargin} />
      <Box
        sx={{
          backgroundImage: "url(" + require("../assets/peakpx.jpg") + ")",
          backgroundRepeat: "no-repeat",
          width: "100vw",
          height: "100vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        {submit ? (
          <Box sx={{ maxHeight: "70vh", width: "70vw", overflowY: "auto" }}>
            <CustomizedAccordian notams={notams} />
          </Box>
        ) : submitClicked ? (
          <CircularProgress sx={{ color: "white" }} size={100} />
        ) : (
          <Grid
            container
            spacing={2}
            columns={24}
            justifyContent="center"
            alignItems="center"
            direction="column"
            sx={{
              zIndex: "1300",
              bgcolor: "white",
              marginLeft: "35%",
              marginRight: "35%",
              height: "200px",
              borderRadius: "20px",
              opacity: "0.9",
            }}
          >
            <Grid item xs={8}>
              <AirportFilter
                fieldLabel="Departure Airport"
                setAirport={setDepartureAirport}
              />
            </Grid>
            <Grid item xs={8}>
              <AirportFilter
                fieldLabel="Arrival Airport"
                setAirport={setArrivalAirport}
              />
            </Grid>
            <Grid item xs={4}>
              <button
                style={{
                  width: "100%",
                  color: "black",
                  backgroundColor: "transparent",
                  border: "1px solid grey",
                  cursor: "pointer",
                  borderRadius: "5px",
                  padding: "8px 105px",
                  marginBottom: "6px",
                }}
                onClick={(e) => handleSubmit(e)}
              >
                Submit
              </button>
            </Grid>
          </Grid>
        )}
      </Box>
    </React.Fragment>
  );
}
