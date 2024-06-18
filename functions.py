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
            print("Invalid input, please enter a number.")

# Function to fetch jokes from the API based on the search term
def fetch_jokes(search_term, limit=1000):
    headers = {
        'Accept': 'application/json',
        
    }
    try:
        response = requests.get('https://icanhazdadjoke.com/search', headers=headers, params={'term': search_term, 'limit': limit}, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        jokes = response.json().get('results')
        return jokes
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

# Function to display jokes in batches
def display_jokes(jokes_list, number_of_jokes):
    start_time = time.time()
    for index in range(0, len(jokes_list), number_of_jokes):
        if time.time() - start_time >= 60:
            break  # Stop after 1 minute
        current_batch = jokes_list[index:index + number_of_jokes]
        print(f"--- Fetching jokes at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
        for joke in current_batch:
            print(f"Joke: {joke}")
        time.sleep(15)  # Wait for 15 seconds before displaying the next batch

# Main function to run the script
def main():
    search_term = input("Enter the search term for the jokes: ").strip()
    number_of_jokes = get_user_input("Enter the number of jokes you want in each set: ")
    
    jokes = fetch_jokes(search_term)
    
    if not jokes:
        print("No jokes found for your search term. Try again.")
        return  # Exit the script if no jokes are found
    
    displayed_jokes = list(set(joke['joke'] for joke in jokes))
    display_jokes(displayed_jokes, number_of_jokes)
    print("Displayed all possible jokes.")

if __name__ == "__main__":
    main()
