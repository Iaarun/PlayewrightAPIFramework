from data.payloads import seed_product_payload, create_product_payload, updated_product_payload
from utils.assertions import assert_status_code


class TestProductsAPI:

    def test_get_single_product(self, api_client, endpoints):
        response = api_client.get(endpoints["single_product"])
        assert_status_code(response, 200)

        response_json = response.json()
        expected = seed_product_payload().to_dict(include_id=True)

        assert response_json["id"] == expected["id"]
        assert response_json["title"] == expected["title"]
        assert response_json["price"] == expected["price"]
        assert response_json["description"] == expected["description"]
        assert response_json["category"] == expected["category"]
        assert response_json["image"] == expected["image"]
        assert response_json["rating"]["rate"] == expected["rating"]["rate"]
        assert response_json["rating"]["count"] == expected["rating"]["count"]

    def test_get_all_products(self, api_client, endpoints):
        response = api_client.get(endpoints["all_products"])
        assert_status_code(response, 200)

        response_json = response.json()
        assert isinstance(response_json, list)
        assert len(response_json) > 0

    def test_create_product(self, api_client, endpoints):
        payload = create_product_payload().to_dict(include_id=False)

        response = api_client.post(endpoints["create_product"], payload)
        assert response.status in [200, 201], (
            f"Expected status 200 or 201, got {response.status}. Body: {response.text()}"
        )

        response_json = response.json()
        assert "id" in response_json
        assert response_json["title"] == payload["title"]
        assert response_json["price"] == payload["price"]
        assert response_json["description"] == payload["description"]
        assert response_json["category"] == payload["category"]
        assert response_json["image"] == payload["image"]
        assert response_json["rating"]["rate"] == payload["rating"]["rate"]
        assert response_json["rating"]["count"] == payload["rating"]["count"]

    def test_update_product(self, api_client, endpoints):
        payload = updated_product_payload().to_dict(include_id=True)

        response = api_client.put(endpoints["update_product"], payload)
        assert_status_code(response, 200)

        response_json = response.json()
        assert response_json["id"] == payload["id"]
        assert response_json["title"] == payload["title"]
        assert response_json["price"] == payload["price"]
        assert response_json["description"] == payload["description"]
        assert response_json["category"] == payload["category"]
        assert response_json["image"] == payload["image"]
        assert response_json["rating"]["rate"] == payload["rating"]["rate"]
        assert response_json["rating"]["count"] == payload["rating"]["count"]

    def test_delete_product(self, api_client, endpoints):
        response = api_client.delete(endpoints["delete_product"])
        assert response.status in [200, 204], (
            f"Expected status 200 or 204, got {response.status}. Body: {response.text()}"
        )

        get_response = api_client.get(endpoints["single_product"])
        assert get_response.status == 404, (
            f"Expected deleted product to return 404, got {get_response.status}. Body: {get_response.text()}"
        )