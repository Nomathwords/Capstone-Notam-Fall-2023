import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import { Typography } from "@mui/material";
import { makeStyles } from "@mui/styles";
import Box from "@mui/material/Box";
import logo from "../assets/plane.svg";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";

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
        <Grid
          container
          spacing={2}
          columns={16}
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
            <TextField
              required
              id="filled-basic"
              label="Required"
              defaultValue="Departure Airport"
            />
          </Grid>
          <Grid item xs={8}>
            <TextField
              required
              id="filled-basic"
              label="Required"
              defaultValue="Arrival Airport"
            />
          </Grid>
        </Grid>
      </Box>
    </React.Fragment>
  );
}
