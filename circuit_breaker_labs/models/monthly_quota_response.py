from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonthlyQuotaResponse")


@_attrs_define
class MonthlyQuotaResponse:
    """
    Attributes:
        generated_tests (int): Number of test cases generated this month.
        alloted_test_generations (int): Total number of test cases allotted for this month.
    """

    generated_tests: int
    alloted_test_generations: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generated_tests = self.generated_tests

        alloted_test_generations = self.alloted_test_generations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "generated_tests": generated_tests,
                "alloted_test_generations": alloted_test_generations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        generated_tests = d.pop("generated_tests")

        alloted_test_generations = d.pop("alloted_test_generations")

        monthly_quota_response = cls(
            generated_tests=generated_tests,
            alloted_test_generations=alloted_test_generations,
        )

        monthly_quota_response.additional_properties = d
        return monthly_quota_response

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
