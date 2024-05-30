import requests
import time

def search_searx(query, max_retries=3):
    searx_url = 'http://localhost:8002/'
    params = {
        'q': query,
        'format': 'json'
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(searx_url, params=params)
            response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
            data = response.json()
            return data['results']
        except requests.RequestException as e:
            print(f"Error fetching data (attempt {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print("Retrying after 5 seconds...")
                time.sleep(5)
            else:
                print("Max retries exceeded.")
                return []

def print_search_results(results):
    if results:
        for result in results:
            print(f"Title: {result['title']}")
            print(f"URL: {result['url']}")
            print(f"Content: {result['content']}")
            print(f"Source: {result['engine']}")
            print()
    else:
        print("No results found.")

# Example usage
query = "stencil thickness"
results = search_searx(query)
print_search_results(results)
