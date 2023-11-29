# Keywords
high = ["OUT OF SERVICE", " OTS", "OTS/BROKEN" "HIJACKING", "BOMB THREAT", "INCURSION", "FIRE EMERGENCY", "FUEL", 
        "WIND SHEAR", "AERODROME LIGHTING", "VIP", "AERODROME CLOSED", "AERODROME CLSD", "AERODROME USE CAUTION", 
        "PROHIBITED", "TEMPORARY FLIGHT RESTRICTIONS", "TWR CLSD", "AERODROME MILITARY ACFT"]

high_noncontiguous = [(("RUNWAY", "CLOSED"), ("RUNWAY", "CLSD"), ("RWY", "CLOSED"), ("RWY", "CLSD"), 
                       ("AIRPORT", "CLOSED"), ("AIRPORT", "CLSD"), (" AP ", "CLOSED"), (" AP ", "CLSD"),
                       ("HAZARD",),)]

medium = ["NAVIGATION AIDS", "EQUIPMENT MAINTENANCE", "COMMUNICATIONS ISSUES", "MILITARY EXERCISES", 
         "VFR/IFR CONDITIONS", "AIR TRAFFIC CONTROL", "RESTRICTED", "LIGHTING", "SQUAWK", "PROCEDURE NA", 
         "RADAR APPROACH CLOSED", "UNUSABLE"]

medium_noncontiguous = [(("DRONE", "FLIGHT OPERATIONS"), ("AIRSPACE", "MOA"),)]

low = ["WILDLIFE HAZARD", "CONSTRUCTION", "ROADWORK", "FUEL PRICE CHANGE", "LOCAL EVENTS", 'FIREFIGHTER',
       "GPS INTERFERENCE", "SVC TAR U/S", "ROUTE", "AIRSPACE UAS", "NOT STD", "EXCAVATION", "WIP", 
       "ALTIMETER UNREL", "UNSERVICEABLE", "SIGN", "CRANE", "OBST", "OBSTACLE", "SPEED RESTRICTION", 
       "FOD", "UNREL", "AIRSPACE CANNON", "APP CLSD", "NOT MNT", "NOT AUTHORIZED", "TAKEOFF MINIMUMS",
       "MARKINGS", "OUT FOR MAINTENANCE", "CHART", "SPECIAL", "AIRSPACE", " ACT", "TEMPORARY RIG",
       "ALL OTHER DATA REMAINS AS PUBLISHED", "DME REQUIRED", "NA OR ONLY USABLE", " CAT", "AMDT",
       "UNMANNED ACFT", "NO-NOTAM MP", "NEAR MOV AREAS", "OPN DLY", "CAUTION", "PATCHY ICE", "IRREGULAR",
       "CIRCLING", "UNMONITORED", "COMMISSIONED", "COMPACTED SN", "WET SN", "HOURS", "NOW PRIVATE",
       "UNABLE TO BROADCAST TRANSMISSIONS", "UNABLE TO SUPPORT", "FICON ICE", "DRY SN", "UAS", "TAX OPS",
       "FLIP CHANGE IN PROGRESS", "PROCEDURE TURN COMPLETION ALTITUDE", "CPDLC AVBL", " NA ", "AERODROME PAEW",
       "TAXI OPERATIONS APPROVED AT THE FOLLOWING LOCATIONS", "TEMPORARY TAXIWAYS", "TFC PATTERN",
       "MINIMUM ALTITUDE", "REMOTE COM", "WIND CONE NOT ILLUMINATED", "LOCALIZER DEGRADED", "LIMITED TO", 
       "BASH PHASE", "NONMOVEMENT AREA", "NOT VISIBLE", "SUTABLE FOR VFR LANDING ONLY", "NOT ROTATING",
       "AIRFIELD PROCEDURES GUIDE", "CONTINUE TO OPERATE", "AERODROME MARINE CORPS", "WILL BE CLOSED",
       "WORKING IN VICINITY", "WORKING IN THE VICINITY", "TRANSMISSION LINE TOWERS", "THR DISPLACED",
       "BASE CLSD", "INTRUSIVE OPERATIONS", "IN THE EVENT OF MISSED APPROACH", "NOT INSTALLED", "BASE CLSD", 
       "INTRUSIVE OPERATIONS", "IN THE EVENT OF MISSED APPROACH", "DEPARTURE", "APPROVED PPR", "RUN UPS",
       "REQUIRED MIN CLIMB", "MIN ALT", "NOT COINCIDENT", "U/S"]

low_noncontiguous = [(("COM VOICE", "CHANGED"), ("TWY", "CLSD"), ("TWY", "CLOSED"), ("RAMP", "CLSD"),
                      ("RAMP", "CLOSED"), ("NOT", "AVBL"), ("NOT", "AVAILABLE"), ("LIGHTS", "O/S"),
                      ("TXL", "CLSD"), ("TXL", "CLOSED"), ("TAXILANE", "CLSD"), ("TAXILANE", "CLOSED"),
                      ("CHANGE", "TO"), ("CHG", "TO"), ("RUNUP PAD", "CLSD"), ("RUNUP PAD", "CLOSED"), 
                      ("PCT", "WET"), ("PCT", "ICE"), ("APRON", "CLOSED"), ("APRON", "CLSD"), ("APN", "CLSD"),
                      ("APN", "CLOSED"), ("SPOT", "CLSD"), ("SPOT", "CLOSED"), ("RWY", "NOW"), 
                      ("CROSS", "AT OR ABOVE"), ("UNLIGHTED", "TOWER"))]

def determine_rank(notams):
    for notam in notams:

        # Variable used to restart the loop correctly. Needed when using a for loop to check for keywords
        found_keyword = False

        # Check for high importance keywords not directly next to each other
        for tuple in high_noncontiguous: # Grab a tuple
            for keywords in tuple: # Grab the keywords in the tuple
                if all(singular_keyword in notam["text"] for singular_keyword in keywords): # Check for each keyword

                    # Make sure WILDLIFE HAZARD is not ranked as High
                    if "HAZARD" in keywords and "WILDLIFE HAZARD" in notam["text"]:
                        continue

                    notam["CS4273_Keywords"] = keywords
                    notam["CS4273_Rank"] = "High"
                    found_keyword = True
                    break  # Break out of the inner loop

            if found_keyword:
                break  # Break out of the outer loop

        # If a high importance noncontiguous keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue
    
        # Check for other high importance keywords
        for keyword in high:
            if keyword in notam["text"]:
                notam["CS4273_Keywords"] = keyword
                notam["CS4273_Rank"] = "High"
                found_keyword = True
                break
    
        # If a high importance keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue

        # Check for medium importance keywords not directly next to each other
        for tuple in medium_noncontiguous: # Grab a tuple
            for keywords in tuple: # Grab the keywords in the tuple
                if all(singular_keyword in notam["text"] for singular_keyword in keywords): # Check for each keyword
                    notam["CS4273_Keywords"] = keywords
                    notam["CS4273_Rank"] = "Medium"
                    found_keyword = True
                    break  # Break out of the inner loop

            if found_keyword:
                break  # Break out of the outer loop

        # If a medium importance noncontiguous keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue

        # Check for other medium importance keywords
        for keyword in medium:
            if keyword in notam["text"]:
                notam["CS4273_Keywords"] = keyword
                notam["CS4273_Rank"] = "Medium"
                found_keyword = True
                break

        # If a medium importance keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue

        # Check for low importance keywords not directly next to each other
        for tuple in low_noncontiguous: # Grab a tuple
            for keywords in tuple: # Grab the keywords in the tuple
                if all(singular_keyword in notam["text"] for singular_keyword in keywords): # Check for each keyword
                    notam["CS4273_Keywords"] = keywords
                    notam["CS4273_Rank"] = "Low"
                    found_keyword = True
                    break  # Break out of the inner loop

            if found_keyword:
                break  # Break out of the outer loop

        # If a low importance noncontiguous keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue
        
        # Check for other low importance keywords
        for keyword in low:
            if keyword in notam["text"]: 
                notam["CS4273_Keywords"] = keyword           
                notam["CS4273_Rank"] = "Low"
                found_keyword = True
                break

        # If a low keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue
        
        # No keyword has been found
        notam["CS4273_Rank"] = "Other"

    return notams