import requests 
import re 
from bs4 import BeautifulSoup 

def fetch_file_content(url): 
    """Fetch the content of a file from a given URL.""" 
    response = requests.get(url) 
    response.raise_for_status() 
    return response.text 

def extract_urls(text): 
    """Extract all URLs from the given text.""" 
    url_pattern = re.compile(r'https?://\S+') 
    return url_pattern.findall(text) 

def main(): # List of file URLs in the GitHub repository 
    file_urls = [ 
        'https://raw.githubusercontent.com/BYUI2023OJS/wdd130/main/wwr/about.html', 
        'https://raw.githubusercontent.com/BYUI2023OJS/wdd130/main/wwr/about.css', 
        # Add more file URLs as needed 
        ] 
    
    all_urls = [] 
    for file_url in file_urls: 
        try: 
            content = fetch_file_content(file_url) 
            urls = extract_urls(content) 
            all_urls.extend(urls) 
        except requests.exceptions.RequestException as e: 
            print(f"Error fetching {file_url}: {e}") 
            
            # Print all extracted URLs 
            for url in all_urls: 
                print(url) 
        if __name__ == "__main__":
            main()