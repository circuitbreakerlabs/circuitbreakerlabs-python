from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="EvaluationResultSummaryResponse")


@_attrs_define
class EvaluationResultSummaryResponse:
    """
    Attributes:
        test_result_id (int):
        evaluation_id (int):
        test_case_id (int | None):
        initial_user_input (None | str):
        passed (bool | None):
        score (float | None):
        model_response (None | str):
        created_at (datetime.datetime):
    """

    test_result_id: int
    evaluation_id: int
    test_case_id: int | None
    initial_user_input: None | str
    passed: bool | None
    score: float | None
    model_response: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_result_id = self.test_result_id

        evaluation_id = self.evaluation_id

        test_case_id: int | None
        test_case_id = self.test_case_id

        initial_user_input: None | str
        initial_user_input = self.initial_user_input

        passed: bool | None
        passed = self.passed

        score: float | None
        score = self.score

        model_response: None | str
        model_response = self.model_response

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_result_id": test_result_id,
                "evaluation_id": evaluation_id,
                "test_case_id": test_case_id,
                "initial_user_input": initial_user_input,
                "passed": passed,
                "score": score,
                "model_response": model_response,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        test_result_id = d.pop("test_result_id")

        evaluation_id = d.pop("evaluation_id")

        def _parse_test_case_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        test_case_id = _parse_test_case_id(d.pop("test_case_id"))

        def _parse_initial_user_input(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        initial_user_input = _parse_initial_user_input(d.pop("initial_user_input"))

        def _parse_passed(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        passed = _parse_passed(d.pop("passed"))

        def _parse_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        score = _parse_score(d.pop("score"))

        def _parse_model_response(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model_response = _parse_model_response(d.pop("model_response"))

        created_at = isoparse(d.pop("created_at"))

        evaluation_result_summary_response = cls(
            test_result_id=test_result_id,
            evaluation_id=evaluation_id,
            test_case_id=test_case_id,
            initial_user_input=initial_user_input,
            passed=passed,
            score=score,
            model_response=model_response,
            created_at=created_at,
        )

        evaluation_result_summary_response.additional_properties = d
        return evaluation_result_summary_response

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
