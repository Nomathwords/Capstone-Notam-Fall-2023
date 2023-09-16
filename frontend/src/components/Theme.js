import { createTheme } from "@mui/material";

const arcBlue = "#0b72b9";
const arcOrange = "#FFBA60";

export default createTheme({
  palette: {
    common: {
      blue: `${arcBlue}`,
      orange: `${arcOrange}`,
    },
    primary: {
      main: `${arcBlue}`,
    },
    secondary: {
      main: `${arcOrange}`,
    },
  },
  typography: {
    h3: {
      fontWeight: 300,
    },
  },
});
