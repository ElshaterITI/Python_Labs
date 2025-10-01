import json
import decorator_task
@decorator_task.log_time
def transform_product_data():
    products = input("Enter your list of products (comma-separted)").split(",")
    prices = list(map(int,input(f"Enter your list of prices (comma-separted) ({len(products)})").split(",")))
    
    products_with_prices = zip(products,prices)
    filtered_products_with_prices = filter(lambda pair: pair[1] > 0, products_with_prices)
    
    dictionarized_products_with_prices = [{
        "product": product,
        "price" : price,
        "discounted" : price * 0.9
    }
    for product, price in filtered_products_with_prices]
    myjson = json.dumps(dictionarized_products_with_prices)
    file = open("products.json",'w')
    file.write(myjson)
    print("Your products and prices have been converted to json sucessfuly!")
