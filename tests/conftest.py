import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

from config.settings import BASE_URL, DEFAULT_HEADERS
from utils.api_client import APIClient
from data.payloads import seed_product_payload


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers=DEFAULT_HEADERS
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def api_client(api_request_context: APIRequestContext) -> APIClient:
    return APIClient(api_request_context)


@pytest.fixture(scope="session")
def endpoints():
    return {
        "single_product": "/products/1",
        "all_products": "/products",
        "create_product": "/products",
        "update_product": "/products/1",
        "delete_product": "/products/1"
    }


@pytest.fixture(autouse=True)
def ensure_product_1_exists(api_client, endpoints):
    response = api_client.get(endpoints["single_product"])

    if response.status == 404:
        all_products_response = api_client.get(endpoints["all_products"])
        assert all_products_response.status == 200, (
            f"Unable to read products list. Body: {all_products_response.text()}"
        )

        products = all_products_response.json()
        product_1 = seed_product_payload().to_dict(include_id=True)

        matching = [p for p in products if p.get("id") == 1]

        if matching:
            api_client.put(endpoints["update_product"], product_1)
        else:
            api_client.post(endpoints["create_product"], product_1)

    yield