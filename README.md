 # MOST ELECTED NAME FOR CONGRESSPEOPLE IN BRAZIL'S 2022 ELECTION
#### Video Demo:  <URL HERE>
#### Description: Python program that counts and ranks the first name of all congresspeople from the 2023-2026 term to find the most popular name for congresspeople

This Python program analyzes the names of federal deputies (congresspeople) from the 57th legislature of Brazil, as listed on Wikipedia. It extracts the names of the deputies, cleans them by removing professional titles, counts the frequency of each first name, and displays the results in descending order. The results are also saved to a text file for further reference.

### Features
+ Web Scraping: The program fetches the HTML content of a Wikipedia page containing a list of federal deputies.
+ Name Extraction: It extracts the names of the deputies from the HTML tables.
+ Name Cleaning: Professional titles such as "Dr.", "Col.", "Professor", etc., are removed from the names.
+ Name Counting: The program counts how many deputies share the same first name.
+ Sorting and Display: The names are sorted by frequency in descending order and displayed to the user.
+ File Saving: The results are saved to a text file (names_rank.txt) for future reference.

### How it workds
+ Fetching Data: The program uses the requests library to fetch the HTML content of the Wikipedia page.
+ Parsing HTML: The BeautifulSoup library is used to parse the HTML and extract the names of the deputies from the tables.
+ Cleaning Names: Professional titles are removed from the names to ensure accurate counting.
+ Counting Names: The program counts how many deputies share the same first name and stores the results in a dictionary.
+ Sorting and Displaying: The dictionary is sorted by frequency, and the results are displayed to the user.
+ Saving Results: The sorted results are saved to a text file for future reference.

### Limitations
+ The program assumes that the first word in each name is the first name. If the names are formatted differently, the results may not be accurate.
+ The program is designed to work with the specific structure of the Wikipedia page for the 57th legislature of Brazil. If the page structure changes, the program may need to be updated.