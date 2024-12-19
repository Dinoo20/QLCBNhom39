def stats_cart(cart):
    if not cart:
        return {"total_amount": 0, "total_quantity": 0}

    total_amount, total_quantity = 0, 0

    for c in cart.values():
        total_quantity += c['quantity']
        total_amount += c['quantity'] * c['price']

    return {
        "total_amount": total_amount,
        "total_quantity": total_quantity
    }
