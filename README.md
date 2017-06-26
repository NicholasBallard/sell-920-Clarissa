# sell-920-Clarissa
web scraper for names/info of property owners in Oakland, Pittsburgh, PA to make a marketing list

\\#1	Go into the Excel file. This is where to maintain the list of street names. The street names will go into the Allegheny county search field for properties.

\\#2	Export the list into a text file. One street name per line. Alternatively, use it to list different parts of the LOT ID.

\\#3	The python script will read the text file listing the street names or LOT IDs.

\\#4	Import beautiful soup. Navigate to Allegheny County Real Estate Portal.


<a href="http://www2.county.allegheny.pa.us/RealEstate/search.aspx">Allegheny County Real Estate Portal</a>

\\#5	Enter first line of text file into the appropriate field. Make sure the right search type is selected, "By Address" or "By Parcel Number".

\\#6	Start the search. Find the first search result link. If in the appropiate wards (likely Ward 4 or Ward 5), then go to the result link.

\\#7	Scrape the names of the owner, when the property was bought, and the mailing address, as well as the property address.

\\#8	Write the information to a python dictionary. Later this will go into a database or Excel file.
