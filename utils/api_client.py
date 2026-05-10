from playwright.sync_api import APIRequestContext, APIResponse


class APIClient:
    def __init__(self, request_context: APIRequestContext):
        self.request_context = request_context

    def get(self, endpoint: str) -> APIResponse:
        return self.request_context.get(endpoint)

    def post(self, endpoint: str, payload: dict) -> APIResponse:
        return self.request_context.post(endpoint, data=payload)

    def put(self, endpoint: str, payload: dict) -> APIResponse:
        return self.request_context.put(endpoint, data=payload)

    def delete(self, endpoint: str) -> APIResponse:
        return self.request_context.delete(endpoint)