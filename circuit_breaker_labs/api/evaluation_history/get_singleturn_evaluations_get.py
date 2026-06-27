from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.evaluation_result_summary_response import EvaluationResultSummaryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    cbl_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["cbl-api-key"] = cbl_api_key

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/singleturn_evaluations",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[EvaluationResultSummaryResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EvaluationResultSummaryResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[EvaluationResultSummaryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    cbl_api_key: str,
) -> Response[HTTPValidationError | list[EvaluationResultSummaryResponse]]:
    """List Historic Single-turn Evaluations

     Return historic single-turn evaluation results for the authenticated user.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        cbl_api_key (str): Circuit Breaker Labs API Key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[EvaluationResultSummaryResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        cbl_api_key=cbl_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    cbl_api_key: str,
) -> HTTPValidationError | list[EvaluationResultSummaryResponse] | None:
    """List Historic Single-turn Evaluations

     Return historic single-turn evaluation results for the authenticated user.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        cbl_api_key (str): Circuit Breaker Labs API Key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[EvaluationResultSummaryResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        cbl_api_key=cbl_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    cbl_api_key: str,
) -> Response[HTTPValidationError | list[EvaluationResultSummaryResponse]]:
    """List Historic Single-turn Evaluations

     Return historic single-turn evaluation results for the authenticated user.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        cbl_api_key (str): Circuit Breaker Labs API Key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[EvaluationResultSummaryResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        cbl_api_key=cbl_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    cbl_api_key: str,
) -> HTTPValidationError | list[EvaluationResultSummaryResponse] | None:
    """List Historic Single-turn Evaluations

     Return historic single-turn evaluation results for the authenticated user.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        cbl_api_key (str): Circuit Breaker Labs API Key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[EvaluationResultSummaryResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            cbl_api_key=cbl_api_key,
        )
    ).parsed
