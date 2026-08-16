# ============================================================
# Part A & B — Mutable Default Argument Bug and Fix
# ============================================================

# BUGGY VERSION (kept here as reference/comment):
# def add_item(item, cart=[]):
#     cart.append(item)
#     return cart
# Bug: cart=[] is created ONCE at function definition time, not on
# each call. Every call that skips the cart argument reuses and
# mutates that same shared list, so values leak between calls.

def add_item(item, cart=None):
    if cart is None:
        cart = []  # fresh list created every call, no shared state
    cart.append(item)
    return cart


# ============================================================
# Part C — Shopping Cart Program
# ============================================================

def create_cart(owner, discount=0):
    # discount=0 is a safe default because int is immutable
    # "items": [] is created fresh inside the function body each call,
    # so different carts never share the same list object
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
    # Tuples are immutable: there is no __setitem__ support, so
    # assigning to an index like price_tuple[0] = new_price would
    # raise a TypeError. Instead of attempting the assignment (which
    # would crash the program), we check the type first and explain
    # why it's not allowed. This immutability is what allows tuples
    # to be hashable and safely shared/reused without side effects.
    if isinstance(price_tuple, tuple):
        print(f"Cannot modify {price_tuple} - tuples do not support item assignment.")
        return price_tuple
    else:
        price_tuple[0] = new_price
        return price_tuple


def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]
    discount_amount = subtotal * (cart["discount"] / 100)
    total = subtotal - discount_amount
    return total


def main():
    cart1 = create_cart("Alice", discount=10)
    cart2 = create_cart("Bob")  # uses default discount=0

    add_to_cart(cart1, "Milk", 3.50, qty=2)
    add_to_cart(cart1, "Bread", 2.00)

    add_to_cart(cart2, "Eggs", 4.00, qty=1)

    print("Alice's cart:", cart1)
    print("Bob's cart:", cart2)

    print("Are item lists the same object?", cart1["items"] is cart2["items"])

    print(f"Alice's total: {calculate_total(cart1):.2f}")
    print(f"Bob's total: {calculate_total(cart2):.2f}")

    price_info = ("Milk", 3.50)
    update_price(price_info, 4.00)


main()