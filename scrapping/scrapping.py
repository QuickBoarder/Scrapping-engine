import requests

# Replace the URL with your target URL

def SearchProd(search_query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': 'AIzaSyAPSjB9UHZQMaoJscfkuDkcSu6xVrLhCtM',
        'cx': '15e784d6495d64790'
    }

    response = requests.get(url, params=params)
    result = response.json()

    # print(result)
    finalResponse = {
        'title': result['items'][0]['title'],
        'image': result['items'][0]['pagemap']['cse_thumbnail'][0]['src']
    }

    return finalResponse
    # print(result['items'][0]['pagemap']['cse_thumbnail'][0]['src'])
    # print(result['items'][0]['title'])

# SearchProd("8901277019226")