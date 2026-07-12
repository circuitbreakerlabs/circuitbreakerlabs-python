from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.single_turn_evaluation_result import SingleTurnEvaluationResult


T = TypeVar("T", bound="SingleTurnResponse")


@_attrs_define
class SingleTurnResponse:
    """Payload for single_turn_response messages (Server -> Client).

    Attributes:
        evaluation_id (int): Persisted evaluation run ID.
        total_passed (int): Number of test cases that passed
        total_failed (int): Number of test cases that failed
        results (list[SingleTurnEvaluationResult] | Unset): All persisted single-turn test results.
    """

    evaluation_id: int
    total_passed: int
    total_failed: int
    results: list[SingleTurnEvaluationResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        evaluation_id = self.evaluation_id

        total_passed = self.total_passed

        total_failed = self.total_failed

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "evaluation_id": evaluation_id,
                "total_passed": total_passed,
                "total_failed": total_failed,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.single_turn_evaluation_result import SingleTurnEvaluationResult

        d = dict(src_dict)
        evaluation_id = d.pop("evaluation_id")

        total_passed = d.pop("total_passed")

        total_failed = d.pop("total_failed")

        _results = d.pop("results", UNSET)
        results: list[SingleTurnEvaluationResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = SingleTurnEvaluationResult.from_dict(results_item_data)

                results.append(results_item)

        single_turn_response = cls(
            evaluation_id=evaluation_id,
            total_passed=total_passed,
            total_failed=total_failed,
            results=results,
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
