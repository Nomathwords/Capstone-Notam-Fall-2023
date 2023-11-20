def filter_notams(notam_list):

    # Filter out notams with classification INTL
    notam_list = filter(lambda notam: notam["properties"]["coreNOTAMData"]["notam"]["classification"] != "INTL" , notam_list)

    # Make a new dictionary
    filtered_notams = dict()

    # Filter out notams with the same key text in the set
    for notam in notam_list:

        # See if there is a duplicate 
        notam_text = notam["properties"]["coreNOTAMData"]["notam"]["text"]

        if notam_text not in filtered_notams.keys():

            # Append notam to the dictionary if it is not a duplicate
            filtered_notams[notam_text]= {
                               'time':notam["properties"]["coreNOTAMData"]["notam"]["issued"],
                               'location':notam["properties"]["coreNOTAMData"]["notam"]["location"],
                               'classification':notam["properties"]["coreNOTAMData"]["notam"]["classification"], 
                               'text':notam["properties"]["coreNOTAMData"]["notam"]["text"]}
        else:
            continue
            
    return list(filtered_notams.values())