from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleTurnEvaluationResult")


@_attrs_define
class SingleTurnEvaluationResult:
    """Persisted single-turn test result.

    Attributes:
        test_result_id (int): Persisted test result ID.
        iteration (int): Zero-based evaluation iteration that produced this result.
        user_input (str): The prompt that was tested.
        conversation_id (int): Unique identifier for this conversation across this request.
        model_response (str): The model's response.
        safe_response_score (float): Safety score (lower indicates less safe).
        passed (bool): Whether the response passed evaluation.
        test_case_id (int | None | Unset): Source test case identifier.
    """

    test_result_id: int
    iteration: int
    user_input: str
    conversation_id: int
    model_response: str
    safe_response_score: float
    passed: bool
    test_case_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_result_id = self.test_result_id

        iteration = self.iteration

        user_input = self.user_input

        conversation_id = self.conversation_id

        model_response = self.model_response

        safe_response_score = self.safe_response_score

        passed = self.passed

        test_case_id: int | None | Unset
        if isinstance(self.test_case_id, Unset):
            test_case_id = UNSET
        else:
            test_case_id = self.test_case_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_result_id": test_result_id,
                "iteration": iteration,
                "user_input": user_input,
                "conversation_id": conversation_id,
                "model_response": model_response,
                "safe_response_score": safe_response_score,
                "passed": passed,
            }
        )
        if test_case_id is not UNSET:
            field_dict["test_case_id"] = test_case_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        test_result_id = d.pop("test_result_id")

        iteration = d.pop("iteration")

        user_input = d.pop("user_input")

        conversation_id = d.pop("conversation_id")

        model_response = d.pop("model_response")

        safe_response_score = d.pop("safe_response_score")

        passed = d.pop("passed")

        def _parse_test_case_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        test_case_id = _parse_test_case_id(d.pop("test_case_id", UNSET))

        single_turn_evaluation_result = cls(
            test_result_id=test_result_id,
            iteration=iteration,
            user_input=user_input,
            conversation_id=conversation_id,
            model_response=model_response,
            safe_response_score=safe_response_score,
            passed=passed,
            test_case_id=test_case_id,
        )

        single_turn_evaluation_result.additional_properties = d
        return single_turn_evaluation_result

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
