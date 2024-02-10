from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from pyzbar.pyzbar import decode
import cv2
import numpy as np

def read_barcode_from_url(url):
    try:
        response = requests.get(url)
        img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)

        # Your barcode reading logic here
        barcodes = decode(img)
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            return barcode_data

    except Exception as e:
        print(f"Error: {e}")
        return None

def SearchProd(search_query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': 'AIzaSyAPSjB9UHZQMaoJscfkuDkcSu6xVrLhCtM',
        'cx': '15e784d6495d64790'
    }

    response = requests.get(url, params=params)
    result = response.json()
    imageList = []

    for item in result['items']:
        try:
            imageList.append(item['pagemap']['cse_thumbnail'][0]['src'])
        except Exception as e:
            pass
    print(imageList)

    finalResponse = {
        'title': result['items'][0]['title'],
        'image': imageList
    }

    return finalResponse

# Create your views here.
@api_view(['GET'])
def getImage(request):
    try:
        print('Started reading image..')
        img = request.data['image']

        barcodeNumber= read_barcode_from_url(img)
        print("Barcode Scanned")
        if barcodeNumber:
            data = SearchProd(barcodeNumber)
            return Response({
                'data' : data
                }, status= 200)

    except Exception as e:
        return Response({'Message': 'Error in getting data'}, status=501)
