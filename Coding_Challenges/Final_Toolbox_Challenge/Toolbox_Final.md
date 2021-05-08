# Tool to Identify Rhode Island Marinas in Close Proximity to Stranded Marine Species 
## Useful for Mystic Aquarium Rescue Volunteers

This toolbox takes two sets of data: Mystic Stranded Species csv file and the swmarinas shapefile.
It converts the csv into a shapefile and adds a buffer around the stranded species- the size of the buffer and units of measurement are up to the user.
The tool then takes the buffered stranded species and with the added marinas shapefile, uses the clip feature to clip only marinas that are within a certain proximity of the stranded species.
The proximity is up to the user, since it can be manually entered in script 2. 
This tool can be useful for Mystic Aquarium volunteers / Marine Mammal Rescue Team as a way to identify and contact local marinas in RI that frequently have stranded species nearby. 

***Data are provided in an attached folder***
