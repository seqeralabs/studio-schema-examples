#!/usr/bin/env python3
"""
Hello World - Beautiful Soup Image Scraper
A simple script to fetch top 10 images for "Studios"
"""

import requests
from bs4 import BeautifulSoup

def main():
    print("Hello World! Let's find images of 'Studios'")
    print("-" * 50)

    # Use Wikipedia which is more scraper-friendly
    url = "https://en.wikipedia.org/wiki/Film_studio"

    # Set a user agent to be polite
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        # Fetch the page
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse with Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find image tags - Wikipedia stores images in the content area
        images = soup.find_all('img', limit=10)

        print(f"\nFound {len(images)} images from Wikipedia:\n")

        # Display the image URLs
        for i, img in enumerate(images, 1):
            img_src = img.get('src', 'No URL found')
            # Wikipedia uses protocol-relative URLs, so add https:
            if img_src.startswith('//'):
                img_src = 'https:' + img_src

            alt_text = img.get('alt', 'No description')
            print(f"{i}. {alt_text}")
            print(f"   URL: {img_src}\n")

        print("-" * 50)
        print("Done! 🎉")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching images: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
