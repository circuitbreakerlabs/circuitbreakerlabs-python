from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.not_found_error import NotFoundError


T = TypeVar("T", bound="NotFoundResponse")


@_attrs_define
class NotFoundResponse:
    """404 Not Found response wrapper.

    Attributes:
        detail (NotFoundError): 404 Not Found error response.
    """

    detail: NotFoundError
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
        from ..models.not_found_error import NotFoundError

        d = dict(src_dict)
        detail = NotFoundError.from_dict(d.pop("detail"))

        not_found_response = cls(
            detail=detail,
        )

        not_found_response.additional_properties = d
        return not_found_response

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
