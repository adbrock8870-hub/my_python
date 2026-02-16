import requests

def get_github_file_url_via_api(adbrock8870, my_python, ad_py):
    """Get GitHub file URL using GitHub API"""
    
    # GitHub API endpoint
    api_url = f"https://api.github.com/repos/{adbrock8870}/{my_python}/contents/{ad_py}"
    
    # Make the request
    response = requests.get(api_url)
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        return data['html_url']
    else:
        return f"Error: File not found (Status: {response.status_code})"

# Usage
url = get_github_file_url_via_api("adbrock8870-hub", "my_python", "ad_py")
print(url)  # https://github.com/adbrock8870-hub/my_python/blob/main/ad.py