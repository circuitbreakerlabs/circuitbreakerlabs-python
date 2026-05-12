from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FailedSingleTurnResult")


@_attrs_define
class FailedSingleTurnResult:
    """Details of a failed single-turn test case.

    Attributes:
        user_input (str): The prompt that was tested
        conversation_id (int): Unique identifier for this conversation across this request
        model_response (str): The model's response
        safe_response_score (float): Safety score (lower indicates less safe)
    """

    user_input: str
    conversation_id: int
    model_response: str
    safe_response_score: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_input = self.user_input

        conversation_id = self.conversation_id

        model_response = self.model_response

        safe_response_score = self.safe_response_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_input": user_input,
                "conversation_id": conversation_id,
                "model_response": model_response,
                "safe_response_score": safe_response_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_input = d.pop("user_input")

        conversation_id = d.pop("conversation_id")

        model_response = d.pop("model_response")

        safe_response_score = d.pop("safe_response_score")

        failed_single_turn_result = cls(
            user_input=user_input,
            conversation_id=conversation_id,
            model_response=model_response,
            safe_response_score=safe_response_score,
        )

        failed_single_turn_result.additional_properties = d
        return failed_single_turn_result

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
