from database import get_connection

def get_all_products():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM products"

    cursor.execute(query)

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return products

def get_product_by_id(product_id):
    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM products WHERE product_id = %s"

    cursor.execute(query, (product_id,))
    product = cursor.fetchone()

    cursor.close()
    connection.close()
    
    return product