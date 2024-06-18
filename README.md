<!-- Hello - I have provided two files with different version of the code. As the file names state, one version of the code has functions and one doesn't. They both excute and yeild the same results.  -->


<!-- ######################################Key Components Explained:#####################################
Headers Setup: Sets up the request headers and makes an API call
User Input: Script takes user input for the search term and number of jokes, enhancing interactivity.
API Request: Fetches all jokes that match the search term up to a specified limit in one go. A
Joke Processing: Converts the results into a set to automatically handle duplicate jokes, ensuring each joke is unique.
Display Loop: Iterates through the jokes in fixed intervals, ensuring that it either stops after 1 minute or after all jokes are displayed, whichever comes first.
Efficient Indexing: Uses slicing to handle batches of jokes for each interval, which is straightforward and effective for this use
Timestamps: Each batch of jokes fetched includes a timestamp indicating when they were fetched. This helps in tracking when the information was retrieved, which is particularly useful for logs or historical context.
Readability: Jokes are separated by newlines and clearly marked, improving the overall readability of the output. Each joke is presented with a "Joke:" prefix.
 case. -->



<!-- ############################## How It Works #########################################
User Input:

The script begins by prompting the user to enter a search term for the jokes.
It then asks for the number of jokes to display in each set. The input for the number of jokes is validated to ensure it is a positive integer.
API Request:

The script sets up headers for the API request
An API request is made to https://icanhazdadjoke.com/search with the user-provided search term and a high limit (up to 1000) to fetch all possible jokes that match the search term.
Handling API Response:

The script checks the response from the API. If no jokes are found, it prints a message and exits.
If jokes are found, it stores them in a set to ensure uniqueness and avoid duplicates.
Displaying Jokes:

The script starts a timer to keep track of the 1-minute duration.
It then iterates over the jokes, displaying them in batches based on the user-defined number of jokes per set.
Each set of jokes is displayed every 15 seconds.
If the script has displayed all unique jokes before the 1-minute duration is up, it prints a message indicating that all possible jokes have been displayed and exits.
Error Handling:

The script includes error handling for network issues and HTTP errors to provide feedback in case something goes wrong with the API request.


###############################Code Breakdown #######################
get_user_input(prompt):

Prompts the user for input and ensures the value entered is a positive integer.
Keeps prompting until a valid positive integer is entered.
fetch_jokes(search_term, limit=1000):

Sets up the request headers and makes an API call to fetch jokes based on the provided search term.
Handles potential request exceptions and returns the list of jokes if successful, or an empty list if an error occurs.
display_jokes(jokes_list, number_of_jokes):

Displays jokes in batches every 15 seconds for 1 minute or until all jokes are shown.
Uses a timer to manage the duration and ensure it does not exceed 1 minute.
main():

Main function that orchestrates the script.
Gets user input for the search term and number of jokes per set.
Fetches jokes from the API.
Checks if jokes are available and displays them using the display_jokes function.
Prints a message and exits if no jokes are found for the provided search term.

Example Usage
Run the script.
Enter a search term when prompted (e.g., "dog").
Enter the number of jokes you want in each set (e.g., "2").
The script will fetch and display jokes based on your inputs, showing new jokes every 15 seconds for up to 1 minute. -->
