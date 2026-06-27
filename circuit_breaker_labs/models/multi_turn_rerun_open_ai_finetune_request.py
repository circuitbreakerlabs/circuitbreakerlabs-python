from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MultiTurnRerunOpenAiFinetuneRequest")


@_attrs_define
class MultiTurnRerunOpenAiFinetuneRequest:
    """
    Attributes:
        test_result_id (int):
        threshold (float):
        max_turns (int):
        model_name (str):
    """

    test_result_id: int
    threshold: float
    max_turns: int
    model_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_result_id = self.test_result_id

        threshold = self.threshold

        max_turns = self.max_turns

        model_name = self.model_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_result_id": test_result_id,
                "threshold": threshold,
                "max_turns": max_turns,
                "model_name": model_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        test_result_id = d.pop("test_result_id")

        threshold = d.pop("threshold")

        max_turns = d.pop("max_turns")

        model_name = d.pop("model_name")

        multi_turn_rerun_open_ai_finetune_request = cls(
            test_result_id=test_result_id,
            threshold=threshold,
            max_turns=max_turns,
            model_name=model_name,
        )

        multi_turn_rerun_open_ai_finetune_request.additional_properties = d
        return multi_turn_rerun_open_ai_finetune_request

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
