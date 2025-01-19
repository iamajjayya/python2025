import requests
from bs4 import BeautifulSoup

def find_ad_units(site_url, ad_url):
    try:
        # Fetch the HTML content of the site
        response = requests.get(site_url, timeout=10)
        response.raise_for_status()
        html_content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Search for the ad URL in all tags (e.g., scripts, iframes, links)
        ad_references = []
        for tag in soup.find_all(['script', 'iframe', 'a', 'link', 'img', 'div']):
            if tag.has_attr('src') and ad_url in tag['src']:
                ad_references.append((tag.name, tag['src']))
            elif tag.has_attr('href') and ad_url in tag['href']:
                ad_references.append((tag.name, tag['href']))
            elif ad_url in tag.get_text():
                ad_references.append((tag.name, tag.get_text().strip()))

        # Check if ad references are found
        if ad_references:
            print(f"Found references to the ad URL '{ad_url}' on {site_url}:\n")
            for tag, reference in ad_references:
                print(f"- Tag: {tag}, Reference: {reference}")
        else:
            print(f"No references to the ad URL '{ad_url}' were found on {site_url}.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the site: {e}")

if __name__ == "__main__":
    # Hardcoded URL of the site to check
    site_url = "https://www.mingpao.com/"
    
    # Ad unit URL to look for
    ad_url = "https://dextrin.jp/"

    # Run the check
    find_ad_units(site_url, ad_url)
