from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="FailedMultiTurnResult")


@_attrs_define
class FailedMultiTurnResult:
    """Details of a failed multi-turn conversation.

    Attributes:
        min_safe_response_score (float): Lowest safety score in the conversation
        conversation_id (int): Unique identifier for this conversation across this request
        conversation (list[Message]): Full conversation history in role/content format
    """

    min_safe_response_score: float
    conversation_id: int
    conversation: list[Message]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        min_safe_response_score = self.min_safe_response_score

        conversation_id = self.conversation_id

        conversation = []
        for conversation_item_data in self.conversation:
            conversation_item = conversation_item_data.to_dict()
            conversation.append(conversation_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min_safe_response_score": min_safe_response_score,
                "conversation_id": conversation_id,
                "conversation": conversation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message

        d = dict(src_dict)
        min_safe_response_score = d.pop("min_safe_response_score")

        conversation_id = d.pop("conversation_id")

        conversation = []
        _conversation = d.pop("conversation")
        for conversation_item_data in _conversation:
            conversation_item = Message.from_dict(conversation_item_data)

            conversation.append(conversation_item)

        failed_multi_turn_result = cls(
            min_safe_response_score=min_safe_response_score,
            conversation_id=conversation_id,
            conversation=conversation,
        )

        failed_multi_turn_result.additional_properties = d
        return failed_multi_turn_result

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
