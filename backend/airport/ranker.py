# Keywords
high = ["OUT OF SERVICE", "HIJACKING", "BOMB THREAT", "INCURSION", "FIRE EMERGENCY", "FUEL", 
        "WIND SHEAR", "AERODROME LIGHTING", "VIP MOVEMENT", "AERODROME CLOSED", "AERODROME CLSD", 
        "AERODROME USE CAUTION", "PROHIBITED", "HAZARD", "OBSTACLE", "OBST", "TEMPORARY FLIGHT RESTRICTIONS", 
        "TWR CLSD"]

medium = ["NAVIGATION AIDS", "EQUIPMENT MAINTENANCE", "COMMUNICATIONS ISSUES", "MILITARY EXERCISES", 
         "VFR/IFR CONDITIONS", "AIR TRAFFIC CONTROL", "RESTRICTED", "LIGHTING", "CRANE", "SQUAWK",
         "PROCEDURE NA"]

low = ["RADAR APPROACH CLOSED", "RAMP CLSD", "WILDLIFE ACTIVITY", "CONSTRUCTION", "ROADWORK", 
       "FUEL PRICE CHANGE", "LOCAL EVENTS", "GPS INTERFERENCE", "SVC TAR U/S", "UNUSABLE", "ROUTE",
       "AIRSPACE UAS", "NOT STD", "EXCAVATION"]

def determine_rank(notams):
    for notam in notams:

        # Keyword used to restart the loop correctly. Needed when using a for loop to check for keywords
        found_keyword = False

        # Check for high importance keywords not directly next to each other
        if ((("RUNWAY" in notam["text"] or "RWY" in notam["text"])  and ("CLOSED" in notam["text"] or "CLSD" in notam["text"])) 
            or (("AIRPORT" in notam["text"] or "AP" in notam["text"]) and ("CLOSED" in notam["text"] or "CLSD" in notam["text"]))):

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
        if (("DRONE" in notam["text"] and "FLIGHT OPERATIONS" in notam["text"])):
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
        if ((("TOWER LGT" in notam["text"] or "WIND TURBINE LGT" in notam["text"] or "NAV" in notam["text"] or "RWY" in notam["text"]) and ("U/S" in notam["text"]))
            or ("COM VOICE" in notam["text"] and "CHANGED" in notam["text"]) 
            or ("TWY" in notam["text"] and ("CLSD" in notam["text"] or "CLOSED" in notam["text"]))
            or ("NOT" in notam["text"] and "AVBL" in notam["text"])):

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