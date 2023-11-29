# Keywords
high = ["OUT OF SERVICE", " OTS", "OTS/BROKEN" "HIJACKING", "BOMB THREAT", "INCURSION", "FIRE EMERGENCY", "FUEL", 
        "WIND SHEAR", "AERODROME LIGHTING", "VIP", "AERODROME CLOSED", "AERODROME CLSD", "AERODROME USE CAUTION", 
        "PROHIBITED", "TEMPORARY FLIGHT RESTRICTIONS", "TWR CLSD", "AERODROME MILITARY ACFT"]

medium = ["NAVIGATION AIDS", "EQUIPMENT MAINTENANCE", "COMMUNICATIONS ISSUES", "MILITARY EXERCISES", 
         "VFR/IFR CONDITIONS", "AIR TRAFFIC CONTROL", "RESTRICTED", "LIGHTING", "SQUAWK", "PROCEDURE NA", 
         "RADAR APPROACH CLOSED", "UNUSABLE"]

low = ["WILDLIFE HAZARD", "CONSTRUCTION", "ROADWORK", "FUEL PRICE CHANGE", "LOCAL EVENTS", 'FIREFIGHTER',
       "GPS INTERFERENCE", "SVC TAR U/S", "ROUTE", "AIRSPACE UAS", "NOT STD", "EXCAVATION", "WIP", 
       "ALTIMETER UNREL", "U/S", "UNSERVICEABLE", "SIGN", "CRANE", "OBST", "OBSTACLE", "SPEED RESTRICTION", 
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
       "REQUIRED MIN CLIMB", "MIN ALT", "NOT COINCIDENT"]

def determine_rank(notams):
    for notam in notams:

        # Variable used to restart the loop correctly. Needed when using a for loop to check for keywords
        found_keyword = False

        # Check for high importance keywords not directly next to each other
        if ((("RUNWAY" in notam["text"] or "RWY " in notam["text"]) and ("CLOSED" in notam["text"] or "CLSD" in notam["text"])) 
            or (("AIRPORT" in notam["text"] or "AP " in notam["text"]) and ("CLOSED" in notam["text"] or "CLSD" in notam["text"]))
            or ("HAZARD" in notam["text"] and "WILDLIFE HAZARD" not in notam["text"])):

            notam["CS4273_Rank"] = "High"
            continue
    
        # Check for other high importance keywords
        for keyword in high:
            if keyword in notam["text"]:
                notam["CS4273_Rank"] = "High"
                found_keyword = True
                break
    
        # If a high importance keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue

        # Check for medium importance keywords not directly next to each other
        if (("DRONE" in notam["text"] and "FLIGHT OPERATIONS" in notam["text"])
            or("AIRSPACE" in notam["text"] and "MOA" in notam["text"])):

            notam["CS4273_Rank"] = "Medium"
            continue

        # Check for other medium importance keywords
        for keyword in medium:
            if keyword in notam["text"]:
                notam["CS4273_Rank"] = "Medium"
                found_keyword = True
                break

        # If a medium importance keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue
        
        # Check for low importance keywords not directly next to each other
        if (("COM VOICE" in notam["text"] and "CHANGED" in notam["text"])
            or ("TWY" in notam["text"] and ("CLSD" in notam["text"] or "CLOSED" in notam["text"]))
            or ("RAMP" in notam["text"] and ("CLSD" in notam["text"] or "CLOSED" in notam["text"]))
            or ("NOT" in notam["text"] and ("AVBL" in notam["text"]) or "AVAILABLE" in notam["text"])
            or ("LIGHTS" in notam["text"] and "O/S" in notam["text"])
            or (("TXL" in notam["text"] or "TAXILANE" in notam["text"]) and ("CLSD" in notam["text"] or "CLOSED" in notam["text"]))
            or (("CHANGE" in notam["text"] or "CHG" in notam["text"]) and "TO" in notam["text"])
            or ("RUNUP PAD" in notam["text"] and ("CLSD" in notam["text"] or "CLOSED" in notam["text"]))
            or ("PCT" in notam["text"] and ("WET" in notam["text"] or "ICE" in notam["text"]))
            or (("APRON" in notam["text"] or "APN" in notam["text"]) and ("CLSD" in notam["text"] or "CLOSED" in notam["text"]))
            or ("SPOT" in notam["text"] and ("CLSD" in notam["text"] or "CLOSED" in notam["text"]))
            or ("RWY" in notam["text"] and "NOW" in notam["text"])
            or ("CROSS" in notam["text"] and "AT OR ABOVE" in notam["text"])
            or ("UNLIGHTED" in notam["text"] and "TOWER" in notam["text"])):

            notam["CS4273_Rank"] = "Low"
            continue
        
        # Check for other low importance keywords
        for keyword in low:
            if keyword in notam["text"]:            
                notam["CS4273_Rank"] = "Low"
                found_keyword = True
                break

        # If a low keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue
        
        # No keyword has been found
        notam["CS4273_Rank"] = "Other"

    return notams