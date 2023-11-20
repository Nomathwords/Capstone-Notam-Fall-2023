import * as React from "react";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import Typography from "@mui/material/Typography";
import AiFillCaretDown from "./AiFillCaretDown";

const makeAccordian = (title, content) => {
  return (
    // Set the accordian to opacity 0.8
    <Accordion
      sx={{
        maxHeight: "70%",
        overflowY: "auto",
        bgcolor: "rgba(51, 112, 180, 0.8)",
        color: "white",
      }}
    >
      <AccordionSummary
        expandIcon={<AiFillCaretDown />}
        aria-controls="panel1a-content"
        id="panel1a-header"
      >
        <Typography>{title}</Typography>
      </AccordionSummary>
      <AccordionDetails>
        {/*Map over content with a key*/}
        <ul>
          {content.map((item, index) => (
            <div>
              <Typography key={index}>{item}</Typography>
              <br />
            </div>
          ))}
        </ul>
      </AccordionDetails>
    </Accordion>
  );
};

export default function CustomizedAccordian({ notams }) {
  const highNotams = notams.filter((notam) => notam.CS4273_Rank === "High");
  const mediumNotams = notams.filter((notam) => notam.CS4273_Rank === "Medium");
  const lowNotams = notams.filter((notam) => notam.CS4273_Rank === "Low");
  const otherNotams = notams.filter((notam) => notam.CS4273_Rank === "Other");

  // Get text from each notam
  const highNotamText = highNotams.map((notam) => notam.text);
  const mediumNotamText = mediumNotams.map((notam) => notam.text);
  const lowNotamText = lowNotams.map((notam) => notam.text);
  const otherNotamText = otherNotams.map((notam) => notam.text);

  return (
    <div>
      {highNotams.length > 0 && makeAccordian("High", highNotamText)}
      {mediumNotams.length > 0 && makeAccordian("Medium", mediumNotamText)}
      {lowNotams.length > 0 && makeAccordian("Low", lowNotamText)}
      {otherNotams.length > 0 && makeAccordian("Other", otherNotamText)}
    </div>
  );
}
