def assert_status_code(response, expected_status: int):
    assert response.status == expected_status, (
        f"Expected status code {expected_status}, but got {response.status}. "
        f"Response body: {response.text()}"
    )


def assert_product_fields(actual: dict, expected: dict):
    assert actual["id"] == expected["id"]
    assert actual["title"] == expected["title"]
    assert actual["price"] == expected["price"]
    assert actual["description"] == expected["description"]
    assert actual["category"] == expected["category"]
    assert actual["image"] == expected["image"]
    assert actual["rating"]["rate"] == expected["rating"]["rate"]
    assert actual["rating"]["count"] == expected["rating"]["count"]