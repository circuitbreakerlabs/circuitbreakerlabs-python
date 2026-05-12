from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.failed_single_turn_result import FailedSingleTurnResult


T = TypeVar("T", bound="SingleTurnResponse")


@_attrs_define
class SingleTurnResponse:
    """Payload for single_turn_response messages (Server -> Client).

    Attributes:
        total_passed (int): Number of test cases that passed
        total_failed (int): Number of test cases that failed
        failed_results (list[list[FailedSingleTurnResult]]): Details of each failed test case per iteration layer
    """

    total_passed: int
    total_failed: int
    failed_results: list[list[FailedSingleTurnResult]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        total_passed = self.total_passed

        total_failed = self.total_failed

        failed_results = []
        for failed_results_item_data in self.failed_results:
            failed_results_item = []
            for failed_results_item_item_data in failed_results_item_data:
                failed_results_item_item = failed_results_item_item_data.to_dict()
                failed_results_item.append(failed_results_item_item)

            failed_results.append(failed_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_passed": total_passed,
                "total_failed": total_failed,
                "failed_results": failed_results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failed_single_turn_result import FailedSingleTurnResult

        d = dict(src_dict)
        total_passed = d.pop("total_passed")

        total_failed = d.pop("total_failed")

        failed_results = []
        _failed_results = d.pop("failed_results")
        for failed_results_item_data in _failed_results:
            failed_results_item = []
            _failed_results_item = failed_results_item_data
            for failed_results_item_item_data in _failed_results_item:
                failed_results_item_item = FailedSingleTurnResult.from_dict(failed_results_item_item_data)

                failed_results_item.append(failed_results_item_item)

            failed_results.append(failed_results_item)

        single_turn_response = cls(
            total_passed=total_passed,
            total_failed=total_failed,
            failed_results=failed_results,
        )

        single_turn_response.additional_properties = d
        return single_turn_response

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
