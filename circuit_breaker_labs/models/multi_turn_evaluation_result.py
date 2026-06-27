from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="MultiTurnEvaluationResult")


@_attrs_define
class MultiTurnEvaluationResult:
    """Persisted multi-turn conversation result.

    Attributes:
        test_result_id (int): Persisted test result ID.
        min_safe_response_score (float): Lowest safety score in the conversation.
        conversation_id (int): Unique identifier for this conversation across this request.
        conversation (list[Message]): Full conversation history in role/content format.
        passed (bool): Whether the conversation passed.
        test_case_id (int | None | Unset): Source test case identifier.
    """

    test_result_id: int
    min_safe_response_score: float
    conversation_id: int
    conversation: list[Message]
    passed: bool
    test_case_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        test_result_id = self.test_result_id

        min_safe_response_score = self.min_safe_response_score

        conversation_id = self.conversation_id

        conversation = []
        for conversation_item_data in self.conversation:
            conversation_item = conversation_item_data.to_dict()
            conversation.append(conversation_item)

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
                "min_safe_response_score": min_safe_response_score,
                "conversation_id": conversation_id,
                "conversation": conversation,
                "passed": passed,
            }
        )
        if test_case_id is not UNSET:
            field_dict["test_case_id"] = test_case_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message

        d = dict(src_dict)
        test_result_id = d.pop("test_result_id")

        min_safe_response_score = d.pop("min_safe_response_score")

        conversation_id = d.pop("conversation_id")

        conversation = []
        _conversation = d.pop("conversation")
        for conversation_item_data in _conversation:
            conversation_item = Message.from_dict(conversation_item_data)

            conversation.append(conversation_item)

        passed = d.pop("passed")

        def _parse_test_case_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        test_case_id = _parse_test_case_id(d.pop("test_case_id", UNSET))

        multi_turn_evaluation_result = cls(
            test_result_id=test_result_id,
            min_safe_response_score=min_safe_response_score,
            conversation_id=conversation_id,
            conversation=conversation,
            passed=passed,
            test_case_id=test_case_id,
        )

        multi_turn_evaluation_result.additional_properties = d
        return multi_turn_evaluation_result

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
