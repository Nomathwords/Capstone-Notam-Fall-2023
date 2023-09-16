import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import { Typography } from "@mui/material";
import { makeStyles } from "@mui/styles";

import logo from "../assets/plane.svg";

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
            gap: "15em",
          }}
        >
          <img src={logo} alt="plane logo" className={classes.logo} />
          <Typography color="secondary" variant="h3">
            Enter Flight Information
          </Typography>
        </Toolbar>
      </AppBar>
      <div className={classes.toolBarMargin} />
    </React.Fragment>
  );
}
