from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.failed_single_turn_result import FailedSingleTurnResult
    from ..models.single_turn_evaluation_result import SingleTurnEvaluationResult


T = TypeVar("T", bound="SingleTurnResponse")


@_attrs_define
class SingleTurnResponse:
    """Payload for single_turn_response messages (Server -> Client).

    Attributes:
        total_passed (int): Number of test cases that passed
        total_failed (int): Number of test cases that failed
        failed_results (list[list[FailedSingleTurnResult]]): Details of each failed test case per iteration layer
        results_by_iteration (list[list[SingleTurnEvaluationResult]] | Unset): All persisted test results per iteration
            layer.
    """

    total_passed: int
    total_failed: int
    failed_results: list[list[FailedSingleTurnResult]]
    results_by_iteration: list[list[SingleTurnEvaluationResult]] | Unset = UNSET
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

        results_by_iteration: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.results_by_iteration, Unset):
            results_by_iteration = []
            for results_by_iteration_item_data in self.results_by_iteration:
                results_by_iteration_item = []
                for results_by_iteration_item_item_data in results_by_iteration_item_data:
                    results_by_iteration_item_item = results_by_iteration_item_item_data.to_dict()
                    results_by_iteration_item.append(results_by_iteration_item_item)

                results_by_iteration.append(results_by_iteration_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_passed": total_passed,
                "total_failed": total_failed,
                "failed_results": failed_results,
            }
        )
        if results_by_iteration is not UNSET:
            field_dict["results_by_iteration"] = results_by_iteration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failed_single_turn_result import FailedSingleTurnResult
        from ..models.single_turn_evaluation_result import SingleTurnEvaluationResult

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

        _results_by_iteration = d.pop("results_by_iteration", UNSET)
        results_by_iteration: list[list[SingleTurnEvaluationResult]] | Unset = UNSET
        if _results_by_iteration is not UNSET:
            results_by_iteration = []
            for results_by_iteration_item_data in _results_by_iteration:
                results_by_iteration_item = []
                _results_by_iteration_item = results_by_iteration_item_data
                for results_by_iteration_item_item_data in _results_by_iteration_item:
                    results_by_iteration_item_item = SingleTurnEvaluationResult.from_dict(
                        results_by_iteration_item_item_data
                    )

                    results_by_iteration_item.append(results_by_iteration_item_item)

                results_by_iteration.append(results_by_iteration_item)

        single_turn_response = cls(
            total_passed=total_passed,
            total_failed=total_failed,
            failed_results=failed_results,
            results_by_iteration=results_by_iteration,
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
