import Autocomplete, { createFilterOptions } from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";
import { airports } from "./utils/Airports";

const filterOptions = createFilterOptions({
  matchFrom: "any",
  limit: 5,
  stringify: (option) => `${option.identifier} ${option.label}`,
});

const AirportFilter = ({ fieldLabel, setAirport }) => {
  return (
    <Autocomplete
      disablePortal
      id="airport-filter"
      options={airports}
      sx={{ width: 300 }}
      getOptionLabel={(option) => `${option.identifier} - ${option.label}`}
      filterOptions={filterOptions}
      onChange={(event, newValue) => {
        setAirport(newValue);
      }}
      renderInput={(params) => (
        <TextField
          {...params}
          label={fieldLabel}
          required
          id="standard-search"
          variant="standard"
        />
      )}
    />
  );
};

export default AirportFilter;
