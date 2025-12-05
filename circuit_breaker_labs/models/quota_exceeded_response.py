from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quota_exceeded_error import QuotaExceededError


T = TypeVar("T", bound="QuotaExceededResponse")


@_attrs_define
class QuotaExceededResponse:
    """403 Quota exceeded response wrapper.

    Attributes:
        detail (QuotaExceededError): 403 Forbidden error response for quota limits.
    """

    detail: QuotaExceededError
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
        from ..models.quota_exceeded_error import QuotaExceededError

        d = dict(src_dict)
        detail = QuotaExceededError.from_dict(d.pop("detail"))

        quota_exceeded_response = cls(
            detail=detail,
        )

        quota_exceeded_response.additional_properties = d
        return quota_exceeded_response

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
