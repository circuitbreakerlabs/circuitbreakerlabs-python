from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.validate_api_key_response import ValidateApiKeyResponse
from ...types import Response


def _get_kwargs(
    *,
    cbl_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["cbl-api-key"] = cbl_api_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/validate_api_key",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ValidateApiKeyResponse | None:
    if response.status_code == 200:
        response_200 = ValidateApiKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | ValidateApiKeyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cbl_api_key: str,
) -> Response[HTTPValidationError | ValidateApiKeyResponse]:
    """Validate Api Key

     Validate the provided API key.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidateApiKeyResponse]
    """

    kwargs = _get_kwargs(
        cbl_api_key=cbl_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cbl_api_key: str,
) -> HTTPValidationError | ValidateApiKeyResponse | None:
    """Validate Api Key

     Validate the provided API key.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidateApiKeyResponse
    """

    return sync_detailed(
        client=client,
        cbl_api_key=cbl_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cbl_api_key: str,
) -> Response[HTTPValidationError | ValidateApiKeyResponse]:
    """Validate Api Key

     Validate the provided API key.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidateApiKeyResponse]
    """

    kwargs = _get_kwargs(
        cbl_api_key=cbl_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cbl_api_key: str,
) -> HTTPValidationError | ValidateApiKeyResponse | None:
    """Validate Api Key

     Validate the provided API key.

    Args:
        cbl_api_key (str): Circuit Breaker Labs API Key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidateApiKeyResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            cbl_api_key=cbl_api_key,
        )
    ).parsed
