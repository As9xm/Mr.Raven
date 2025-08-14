import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time

init(autoreset=True)

print('''

     ______  _______        _____               _____          ____    ____      ____      ______  _____   ______   
    |      \/       \   ___|\    \          ___|\    \    ____|\   \  |    |    |    | ___|\     \|\    \ |\     \  
   /          /\     \ |    |\    \        |    |\    \  /    /\    \ |    |    |    ||     \     \\\    \| \     \ 
  /     /\   / /\     ||    | |    |       |    | |    ||    |  |    ||    |    |    ||     ,_____/|\|    \  \     |
 /     /\ \_/ / /    /||    |/____/        |    |/____/ |    |__|    ||    |    |    ||     \--'\_|/ |     \  |    |
|     |  \|_|/ /    / ||    |\    \        |    |\    \ |    .--.    ||    |    |    ||     /___/|   |      \ |    |
|     |       |    |  ||    | |    |       |    | |    ||    |  |    ||\    \  /    /||     \____|\  |    |\ \|    |
|\____\       |____|  /|____| |____|  ___  |____| |____||____|  |____|| \ ___\/___ / ||____ '     /| |____||\_____/|
| |    |      |    | / |    | |    | |   | |    | |    ||    |  |    | \ |   ||   | / |    /_____/ | |    |/ \|   ||
 \|____|      |____|/  |____| |____| |___| |____| |____||____|  |____|  \|___||___|/  |____|     | / |____|   |___|/
    \(          )/       \(     )/           \(     )/    \(      )/      \(    )/      \( |_____|/    \(       )/  
     '          '         '     '             '     '      '      '        '    '        '    )/        '       '   
                                                                                              '                     

''')


time.sleep(2)


def main():
    # Ask the user for the URL
    url = input(Fore.RED + "Enter the URL to crawl: ").strip()
    
    # Ask the user
    limit_input = input(Fore.YELLOW + "Enter the number of links to display (or press Enter for all): ").strip()
    limit = int(limit_input) if limit_input.isdigit() else None
    
    try:
        # Fetch the URL
        response = requests.get(url)
        response.raise_for_status()  # error
        
        # Parse the content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Print the title of the page
        print(Fore.BLUE + "Page Title:", soup.title.string if soup.title else "No title found")
        
        # Extract all links
        print(Fore.BLUE + "\nLinks found on the page:")
        links = soup.find_all('a', href=True)
        for i, link in enumerate(links):
            if limit is not None and i >= limit:
                break
            print(link['href'])
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching the URL: {e}")

if __name__ == "__main__":
    main()