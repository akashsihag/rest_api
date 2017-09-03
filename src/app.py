#!/bin/python
from flask import Flask, jsonify, request, url_for
from decimal import Decimal

app = Flask(__name__)
#Dummy List for Products which will be later generated from Database.
products = [
    {
        'id': 1,
        'productName': u'Galaxy J7 Prime',
        'brand': u'Samsung',
        'ram': u'2 GB',
        'price': 14000.0,
        'description': u'Smartphone', 
        'qty': 10,
        'processor': u'Exynos 4',
        'stockStatus':'in',
        'screenSize': 5.5

    },
    {
        'id': 2,
        'productName': u'iPhone 7',
        'brand': u'Apple',
        'ram': u'2 GB',
        'price': 47000.0,
        'description': u'Smartphone', 
        'qty': 5,
        'processor': u'Intel M',
        'stockStatus':'in',
        'screenSize': 4.7
    },
    {
        'id': 3,
        'productName': u'OnePlus 5',
        'brand': u'OnePlus',
        'ram': u'6 GB',
        'price': 32999.0,
        'description': u'Smartphone', 
        'qty': 3,
        'processor': u'Snapdragon 835',
        'stockStatus':'in',
        'screenSize': 5.5
    },
    {
        'id': 4,
        'productName': u'Yuphoria',
        'brand': u'Yu',
        'ram': u'2GB',
        'price': 6599.0,
        'description': u'Smartphone', 
        'qty': 8,
        'processor': u'Snapdragon S6',
        'stockStatus':'in',
        'screenSize': 5.0
    },
    {
        'id': 5,
        'productName': u'Moto G (2nd Gen)',
        'brand': u'Motorola',
        'ram': u'1 GB',
        'price': 4577.0,
        'description': u'Smartphone', 
        'qty': 14,
        'processor': u'Snapdragon 400',
        'stockStatus':'in',
        'screenSize': 5.0
    },
    {
        'id': 6,
        'productName': u'iPhone 5',
        'brand': u'Apple',
        'ram': u'512 MB',
        'price': 15799.0,
        'description': u'Smartphone', 
        'qty': 37,
        'processor': u'Intel M',
        'stockStatus':'in',
        'screenSize': 4.0
    },
    {
        'id': 7,
        'productName': u'Galaxy Y',
        'brand': u'Samsung',
        'ram': u'512 MB',
        'price': 3299.0,
        'description': u'Smartphone', 
        'qty': 0,
        'processor': u'Broadcom 150',
        'stockStatus':'out',
        'screenSize': 3.5
    },
    {
        'id': 8,
        'productName': u'Redmi Note 4',
        'brand': u'Mi',
        'ram': u'3 GB',
        'price': 1359.90,
        'description': u'Smartphone', 
        'qty': 7,
        'processor': u'Snapdragon 600',
        'stockStatus':'in',
        'screenSize': 5.5
    }
]


# End URL for the API Method, and Type of HTTP Request.
@app.route('/shopping/products', methods=['GET'])
def get_products():
    #Getting arguments from Query URL
    minPrice = request.args.get('minPrice')
    maxPrice = request.args.get('maxPrice')
    productName = request.args.get('productName')
    if minPrice is None:
        minPrice = 0.0
    if maxPrice is None:
        maxPrice = Decimal('Infinity')
    minPrice = float(minPrice)
    maxPrice = float(maxPrice)
    productToSend = []
    #Filtering items in this Loop
    for product in products:
        print product['price']
        if (minPrice < product['price'] and product['price'] < maxPrice):
            if (productName is not None):
                if (productName.lower() in product['productName'].lower()):
                    productToSend.append(product)
                    print product
            else:
                productToSend.append(product)
                print product
    #Converting Array to JSON Object
    return jsonify({'products': productToSend})

if __name__ == '__main__':
    app.run(debug=True)

