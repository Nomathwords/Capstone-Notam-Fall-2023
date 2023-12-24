
''' Below are keywords that frequently appear in NOTAM text. The noncontiguous lists are keywords that we are 
searching for that do not directly follow each other in the text. For example, in a NOTAM that contains the text
'!GYI 01/003 GYI RWY 13/31 CLSD 2101061509-PERM', the important keywords are 'RWY' and 'CLSD'. I have put these
keywords into a list of tuples that will be iterated over. If the keywords in the tuples appear in the text, 
then a rank will be applied to that specific NOTAM. Note that once we find a keyword, we quit looking for any
other keywords and move on to the next NOTAM. '''

high = ["OUT OF SERVICE", " OTS", "OTS/BROKEN", "HIJACKING", "BOMB THREAT", "INCURSION", "FIRE EMERGENCY", "FUEL",
        "WIND SHEAR", "AERODROME LIGHTING", "VIP", "AERODROME CLOSED", "AERODROME CLSD", "AERODROME USE CAUTION", 
        "PROHIBITED", " TEMPORARY FLIGHT RESTRICTIONS", "TWR CLSD", "AERODROME MILITARY ACFT", "AD AP CLSD",
        "HIGH SPEED ACFT", "ABN U/S"]

# HAZARD is not a tuple, but we will check to make sure WILFLIFE HAZARD does not appear in the text
high_noncontiguous = [(("RUNWAY", "CLOSED"), ("RUNWAY", "CLSD"), ("RWY", "CLOSED"), ("RWY", "CLSD"), 
                       ("AIRPORT", "CLOSED"), ("AIRPORT", "CLSD"), ("HAZARD",),)]

medium = ["NAVIGATION AIDS", "EQUIPMENT MAINTENANCE", "COMMUNICATIONS ISSUES", "MILITARY EXERCISES", 
         "VFR/IFR CONDITIONS", "AIR TRAFFIC CONTROL", "RESTRICTED", "LIGHTING", "SQUAWK", "PROCEDURE NA", 
         "RADAR APPROACH CLOSED", "UNUSABLE"]

medium_noncontiguous = [(("DRONE", "FLIGHT OPERATIONS"), ("AIRSPACE", "MOA"),)]

low = ["WILDLIFE HAZARD", "CONSTRUCTION", "ROADWORK", "FUEL PRICE CHANGE", "LOCAL EVENTS", 'FIREFIGHTER',
       "GPS INTERFERENCE", "SVC TAR U/S", "ROUTE", "AIRSPACE UAS", "NOT STD", "EXCAVATION", "WIP", 
       "ALTIMETER UNREL", "UNSERVICEABLE", "SIGN", "CRANE", "OBST", "OBSTACLE", "SPEED RESTRICTION", 
       "FOD", "UNREL", "AIRSPACE CANNON", "APP CLSD", "NOT MNT", "NOT AUTHORIZED", "TAKEOFF MINIMUMS",
       "MARKINGS", "OUT FOR MAINTENANCE", " ACT", "TEMPORARY RIG", "ALL OTHER DATA REMAINS AS PUBLISHED", 
       "DME REQUIRED", "NA OR ONLY USABLE", " CAT", "AMDT", "UNMANNED ACFT", "NO-NOTAM MP", "NEAR MOV AREAS", 
       "OPN DLY", "CAUTION", "PATCHY ICE", "IRREGULAR", "REQUIRED MIN CLIMB", "MIN ALT", "NOT COINCIDENT",
       "CIRCLING", "UNMONITORED", "COMMISSIONED", "COMPACTED SN", "WET SN", "HOURS", "NOW PRIVATE",
       "UNABLE TO BROADCAST TRANSMISSIONS", "UNABLE TO SUPPORT", "FICON ICE", "DRY SN", "UAS", "TAX OPS",
       "FLIP CHANGE IN PROGRESS", "PROCEDURE TURN COMPLETION ALTITUDE", "CPDLC AVBL", " NA ", "AERODROME PAEW",
       "TAXI OPERATIONS APPROVED AT THE FOLLOWING LOCATIONS", "TEMPORARY TAXIWAYS", "TFC PATTERN",
       "MINIMUM ALTITUDE", "REMOTE COM", "WIND CONE NOT ILLUMINATED", "LOCALIZER DEGRADED", "LIMITED TO", 
       "BASH PHASE", "NONMOVEMENT AREA", "NOT VISIBLE", "SUTABLE FOR VFR LANDING ONLY", "NOT ROTATING",
       "AIRFIELD PROCEDURES GUIDE", "CONTINUE TO OPERATE", "AERODROME MARINE CORPS", "WILL BE CLOSED",
       "WORKING IN VICINITY", "WORKING IN THE VICINITY", "TRANSMISSION LINE TOWERS", "THR DISPLACED",
       "BASE CLSD", "INTRUSIVE OPERATIONS", "IN THE EVENT OF MISSED APPROACH", "NOT INSTALLED", "BASE CLSD", 
       "INTRUSIVE OPERATIONS", "IN THE EVENT OF MISSED APPROACH", "DEPARTURE", "APPROVED PPR", "RUN UPS", "U/S"]

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
        notam, found_keyword = rank_noncontiguous_keywords(notam, "High", high_noncontiguous, found_keyword)

        # If a high importance noncontiguous keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue

        # Check for other high importance keywords
        notam, found_keyword = rank_contiguous_keywords(notam, "High", high, found_keyword)
    
        # If a high importance keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue

        # Check for medium importance keywords not directly next to each other
        notam, found_keyword = rank_noncontiguous_keywords(notam, "Medium", medium_noncontiguous, found_keyword)

        # If a medium importance noncontiguous keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue

        # Check for other medium importance keywords
        notam, found_keyword = rank_contiguous_keywords(notam, "Medium", medium, found_keyword)

        # If a medium importance keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue

        # Check for low importance keywords not directly next to each other
        notam, found_keyword = rank_noncontiguous_keywords(notam, "Low", low_noncontiguous, found_keyword)

        # If a low importance noncontiguous keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue
        
        # Check for other low importance keywords
        notam, found_keyword = rank_contiguous_keywords(notam, "Low", low, found_keyword)

        # If a low importance keyword is found, move on to the next NOTAM
        if (found_keyword == True):
            continue
        
        # No keyword has been found
        notam["CS4273_Rank"] = "Other"

    return notams

# Iterate through a list of contiguous keywords, and if found in the text, give the NOTAM a rank
def rank_contiguous_keywords(notam, rank, keyword_list, found_keyword):

    # Remove newlines before checking the text
    cleaned_text = notam["text"].replace('\n', ' ')

    for keyword in keyword_list:
        if keyword in cleaned_text: 
            notam["CS4273_Keywords"] = keyword         
            notam["CS4273_Rank"] = rank
            found_keyword = True
            break
    
    return notam, found_keyword

# Iterate through a list of noncontiguous keywords, and if found in the text, give the NOTAM a rank
def rank_noncontiguous_keywords(notam, rank, keyword_list, found_keyword):

    # Remove newlines before checking the text
    cleaned_text = notam["text"].replace('\n', ' ')

    for tuple in keyword_list: # Grab a tuple
        for keywords in tuple: # Grab the keywords in the tuple
            if all(singular_keyword in cleaned_text for singular_keyword in keywords): # Check for each keyword

                # Make sure WILDLIFE HAZARD is not ranked as High when checking for High keywords
                if (("HAZARD" in keywords and "WILDLIFE HAZARD" in cleaned_text) and (rank == "High")):
                    continue

                notam["CS4273_Keywords"] = keywords
                notam["CS4273_Rank"] = rank
                found_keyword = True
                break  # Break out of the inner loop

        if found_keyword:
            break  # Break out of the outer loop
    
    return notam, found_keyword