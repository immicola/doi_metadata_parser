import requests

def get_metadata(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    
    if response.status_code == 200:
        metadata = response.json()["message"]
        print(f"Title: {metadata.get('title', [''])[0]}")
        print(f"Authors: {', '.join([f'{author.get('given', '')} {author.get('family', '')}' for author in metadata.get('author', [])])}")
        print(f"Publication Year: {metadata.get('issued', {}).get('date-parts', [[None]])[0][0]}")
        print(f"Publisher: {metadata.get('publisher', '')}")
        print(f"Journal: {metadata.get('container-title', [''])[0]}")
        print(f"DOI: {metadata.get('DOI', '')}")
    else:
        print("Failed to retrieve metadata.")

# Example usage
get_metadata("10.1016/j.compind.2023.104007")
