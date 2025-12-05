from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.internal_server_error import InternalServerError


T = TypeVar("T", bound="InternalServerErrorResponse")


@_attrs_define
class InternalServerErrorResponse:
    """500 Internal Server Error response wrapper.

    Attributes:
        detail (InternalServerError): 500 Internal Server Error response.
    """

    detail: InternalServerError
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        detail = self.detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_server_error import InternalServerError

        d = dict(src_dict)
        detail = InternalServerError.from_dict(d.pop("detail"))

        internal_server_error_response = cls(
            detail=detail,
        )

        internal_server_error_response.additional_properties = d
        return internal_server_error_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
