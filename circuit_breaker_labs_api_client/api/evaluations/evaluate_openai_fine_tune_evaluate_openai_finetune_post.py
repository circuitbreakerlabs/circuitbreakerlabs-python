from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.evaluate_open_ai_finetune_request import EvaluateOpenAiFinetuneRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.quota_exceeded_error import QuotaExceededError
from ...models.run_tests_response import RunTestsResponse
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    *,
    body: EvaluateOpenAiFinetuneRequest,
    cbl_api_key: str,
    openai_api_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["cbl-api-key"] = cbl_api_key

    headers["openai-api-key"] = openai_api_key







    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/evaluate_openai_finetune",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = RunTestsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = QuotaExceededError.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EvaluateOpenAiFinetuneRequest,
    cbl_api_key: str,
    openai_api_key: str,

) -> Response[HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError]:
    """Evaluate OpenAI Fine Tune

     Run agentic safety tests against an OpenAI fine-tuned model.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key
        openai_api_key (str):
            The OpenAI API Key owned by a [service account](https://platform.openai.com/docs/api-
            reference/project-service-accounts) within the same project as the finetuned model. The
            API key should minimally have 'Request' permissions for 'Model Capabilities'.

            You can create a new API key associated with a service account and project
            [here](https://platform.openai.com/api-keys).

        body (EvaluateOpenAiFinetuneRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError]

    """
    kwargs = _get_kwargs(
        body=body,
cbl_api_key=cbl_api_key,
openai_api_key=openai_api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: EvaluateOpenAiFinetuneRequest,
    cbl_api_key: str,
    openai_api_key: str,

) -> HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError | None:
    """Evaluate OpenAI Fine Tune

     Run agentic safety tests against an OpenAI fine-tuned model.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key
        openai_api_key (str):
            The OpenAI API Key owned by a [service account](https://platform.openai.com/docs/api-
            reference/project-service-accounts) within the same project as the finetuned model. The
            API key should minimally have 'Request' permissions for 'Model Capabilities'.

            You can create a new API key associated with a service account and project
            [here](https://platform.openai.com/api-keys).

        body (EvaluateOpenAiFinetuneRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError

    """
    return sync_detailed(
        client=client,
body=body,
cbl_api_key=cbl_api_key,
openai_api_key=openai_api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EvaluateOpenAiFinetuneRequest,
    cbl_api_key: str,
    openai_api_key: str,

) -> Response[HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError]:
    """Evaluate OpenAI Fine Tune

     Run agentic safety tests against an OpenAI fine-tuned model.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key
        openai_api_key (str):
            The OpenAI API Key owned by a [service account](https://platform.openai.com/docs/api-
            reference/project-service-accounts) within the same project as the finetuned model. The
            API key should minimally have 'Request' permissions for 'Model Capabilities'.

            You can create a new API key associated with a service account and project
            [here](https://platform.openai.com/api-keys).

        body (EvaluateOpenAiFinetuneRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError]

    """
    kwargs = _get_kwargs(
        body=body,
cbl_api_key=cbl_api_key,
openai_api_key=openai_api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EvaluateOpenAiFinetuneRequest,
    cbl_api_key: str,
    openai_api_key: str,

) -> HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError | None:
    """Evaluate OpenAI Fine Tune

     Run agentic safety tests against an OpenAI fine-tuned model.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key
        openai_api_key (str):
            The OpenAI API Key owned by a [service account](https://platform.openai.com/docs/api-
            reference/project-service-accounts) within the same project as the finetuned model. The
            API key should minimally have 'Request' permissions for 'Model Capabilities'.

            You can create a new API key associated with a service account and project
            [here](https://platform.openai.com/api-keys).

        body (EvaluateOpenAiFinetuneRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QuotaExceededError | RunTestsResponse | UnauthorizedError

    """
    return (await asyncio_detailed(
        client=client,
body=body,
cbl_api_key=cbl_api_key,
openai_api_key=openai_api_key,

    )).parsed
