import requests
import time
from datetime import datetime

# Function to get user input and ensure it is a positive integer
def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input, please enter a number..")

# Set up headers for the API request
headers = {
    'Accept': 'application/json',
    
}

# Get user input for search term and number of jokes
search_term = input("Enter the search term for the jokes: ").strip()
number_of_jokes = get_user_input("Enter the number of jokes you want in each set: ")

try:
    # API request with error handling
    response = requests.get('https://icanhazdadjoke.com/search', headers=headers, params={'term': search_term, 'limit': 1000}, timeout=10)
    response.raise_for_status()  # Check for HTTP errors
    jokes = response.json().get('results')
    #print(Debug: jokes)
   
    
    if not jokes:
        print("No jokes found for your search term. Try again.")
        exit()  # Exit the script if no jokes are found

    # Create a set to store unique jokes to avoid displaying duplicates
    displayed_jokes = set(joke['joke'] for joke in jokes)
    
    # Displaying jokes every 15 seconds
    start_time = time.time()
    jokes_list = list(displayed_jokes)  # Convert set to list for ordered access
    for index in range(0, len(jokes_list), number_of_jokes):
        if time.time() - start_time >= 60:
            break  # Stop after 1 minute
        current_batch = jokes_list[index:index + number_of_jokes]
        print(f"--- Fetching jokes at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
        for joke in current_batch:
            print(f"Joke: {joke}")
        time.sleep(15)  # Wait for 15 seconds before displaying the next batch

except requests.RequestException as e:
    print(f"An error occurred: {e}")

print("Displayed all possible jokes.")
