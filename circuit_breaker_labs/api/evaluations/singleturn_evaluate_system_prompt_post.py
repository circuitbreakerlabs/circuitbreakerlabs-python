from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.internal_server_error_response import InternalServerErrorResponse
from ...models.not_found_response import NotFoundResponse
from ...models.quota_exceeded_response import QuotaExceededResponse
from ...models.single_turn_evaluate_system_prompt_request import SingleTurnEvaluateSystemPromptRequest
from ...models.single_turn_run_tests_response import SingleTurnRunTestsResponse
from ...models.unauthorized_response import UnauthorizedResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SingleTurnEvaluateSystemPromptRequest,
    cbl_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["cbl-api-key"] = cbl_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/singleturn_evaluate_system_prompt",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | InternalServerErrorResponse
    | NotFoundResponse
    | QuotaExceededResponse
    | SingleTurnRunTestsResponse
    | UnauthorizedResponse
    | None
):
    if response.status_code == 200:
        response_200 = SingleTurnRunTestsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = QuotaExceededResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = NotFoundResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = InternalServerErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    HTTPValidationError
    | InternalServerErrorResponse
    | NotFoundResponse
    | QuotaExceededResponse
    | SingleTurnRunTestsResponse
    | UnauthorizedResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SingleTurnEvaluateSystemPromptRequest,
    cbl_api_key: str,
) -> Response[
    HTTPValidationError
    | InternalServerErrorResponse
    | NotFoundResponse
    | QuotaExceededResponse
    | SingleTurnRunTestsResponse
    | UnauthorizedResponse
]:
    """Single-turn Evaluate System Prompt

     Run single-turn safety tests against a system prompt.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key
        body (SingleTurnEvaluateSystemPromptRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InternalServerErrorResponse | NotFoundResponse | QuotaExceededResponse | SingleTurnRunTestsResponse | UnauthorizedResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        cbl_api_key=cbl_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SingleTurnEvaluateSystemPromptRequest,
    cbl_api_key: str,
) -> (
    HTTPValidationError
    | InternalServerErrorResponse
    | NotFoundResponse
    | QuotaExceededResponse
    | SingleTurnRunTestsResponse
    | UnauthorizedResponse
    | None
):
    """Single-turn Evaluate System Prompt

     Run single-turn safety tests against a system prompt.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key
        body (SingleTurnEvaluateSystemPromptRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InternalServerErrorResponse | NotFoundResponse | QuotaExceededResponse | SingleTurnRunTestsResponse | UnauthorizedResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        cbl_api_key=cbl_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SingleTurnEvaluateSystemPromptRequest,
    cbl_api_key: str,
) -> Response[
    HTTPValidationError
    | InternalServerErrorResponse
    | NotFoundResponse
    | QuotaExceededResponse
    | SingleTurnRunTestsResponse
    | UnauthorizedResponse
]:
    """Single-turn Evaluate System Prompt

     Run single-turn safety tests against a system prompt.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key
        body (SingleTurnEvaluateSystemPromptRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InternalServerErrorResponse | NotFoundResponse | QuotaExceededResponse | SingleTurnRunTestsResponse | UnauthorizedResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        cbl_api_key=cbl_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SingleTurnEvaluateSystemPromptRequest,
    cbl_api_key: str,
) -> (
    HTTPValidationError
    | InternalServerErrorResponse
    | NotFoundResponse
    | QuotaExceededResponse
    | SingleTurnRunTestsResponse
    | UnauthorizedResponse
    | None
):
    """Single-turn Evaluate System Prompt

     Run single-turn safety tests against a system prompt.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key
        body (SingleTurnEvaluateSystemPromptRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InternalServerErrorResponse | NotFoundResponse | QuotaExceededResponse | SingleTurnRunTestsResponse | UnauthorizedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            cbl_api_key=cbl_api_key,
        )
    ).parsed
