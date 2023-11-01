def filter_notams(notam_list):
    # Filter out notams with classification INTL
    # properties, coreNOTAMData, notam
    notam_list = filter(lambda notam: notam["properties"]["coreNOTAMData"]["notam"]["classification"] != "INTL" , notam_list)
    
    # Filter out notams with the same key text in the set
    # make a new dictionary
    filtered_notams = dict()
    # iterate over the filtered data
    for notam in notam_list:
        #See if there is a duplicate 
        notam_text = notam["properties"]["coreNOTAMData"]["notam"]["text"]
        if notam_text in filtered_notams.keys():
            continue
        else:
            #append notam to the dictionary if it is not a duplicate
            filtered_notams[notam_text]= {
                               'time':notam["properties"]["coreNOTAMData"]["notam"]["issued"],
                               'location':notam["properties"]["coreNOTAMData"]["notam"]["location"],
                               'classification':notam["properties"]["coreNOTAMData"]["notam"]["classification"], 
                               'text':notam["properties"]["coreNOTAMData"]["notam"]["text"],
                               'rank':"None"}

    return list(filtered_notams.values())