from flask import Blueprint, request
from models.db import get_connection
from utils.response import api_response
product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return api_response(rows)

@product_bp.route("/products", methods=["POST"])
def add_product():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO products (product_name, price, quantity)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (
        data["product_name"],
        data["price"],
        data["quantity"]
    ))
    conn.commit()
    conn.close()
    return api_response(message="Product added", status=201)

@product_bp.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE products
        SET price=%s, quantity=%s
        WHERE product_id=%s
    """, (data["price"], data["quantity"], product_id))
    conn.commit()
    conn.close()
    return api_response(message="Product updated")

@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM products WHERE product_id=%s",
        (product_id,)
    )
    conn.commit()
    conn.close()

    return api_response(message="Product deleted")
