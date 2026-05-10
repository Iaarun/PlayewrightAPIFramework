from data.models import Product, Rating


def seed_product_payload() -> Product:
    return Product(
        id=1,
        title="Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        price=109.95,
        description="Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        category="men's clothing",
        image="https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        rating=Rating(
            rate=3.9,
            count=120
        )
    )


def create_product_payload() -> Product:
    return Product(
        title="New Test Product",
        price=109.95,
        description="Created during API automation test",
        category="men's clothing",
        image="https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        rating=Rating(
            rate=3.9,
            count=120
        )
    )


def updated_product_payload() -> Product:
    return Product(
        id=1,
        title="Updated Fjallraven Backpack",
        price=129.99,
        description="Updated product description for API test validation",
        category="men's clothing",
        image="https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        rating=Rating(
            rate=4.5,
            count=150
        )
    )