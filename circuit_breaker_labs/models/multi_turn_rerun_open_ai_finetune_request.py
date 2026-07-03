from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiTurnRerunOpenAiFinetuneRequest")


@_attrs_define
class MultiTurnRerunOpenAiFinetuneRequest:
    """
    Attributes:
        threshold (float):
        max_turns (int):
        model_name (str):
        test_result_ids (list[int] | None | Unset):
        evaluation_id (int | None | Unset):
    """

    threshold: float
    max_turns: int
    model_name: str
    test_result_ids: list[int] | None | Unset = UNSET
    evaluation_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold = self.threshold

        max_turns = self.max_turns

        model_name = self.model_name

        test_result_ids: list[int] | None | Unset
        if isinstance(self.test_result_ids, Unset):
            test_result_ids = UNSET
        elif isinstance(self.test_result_ids, list):
            test_result_ids = self.test_result_ids

        else:
            test_result_ids = self.test_result_ids

        evaluation_id: int | None | Unset
        if isinstance(self.evaluation_id, Unset):
            evaluation_id = UNSET
        else:
            evaluation_id = self.evaluation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "threshold": threshold,
                "max_turns": max_turns,
                "model_name": model_name,
            }
        )
        if test_result_ids is not UNSET:
            field_dict["test_result_ids"] = test_result_ids
        if evaluation_id is not UNSET:
            field_dict["evaluation_id"] = evaluation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        threshold = d.pop("threshold")

        max_turns = d.pop("max_turns")

        model_name = d.pop("model_name")

        def _parse_test_result_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                test_result_ids_type_0 = cast(list[int], data)

                return test_result_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        test_result_ids = _parse_test_result_ids(d.pop("test_result_ids", UNSET))

        def _parse_evaluation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        evaluation_id = _parse_evaluation_id(d.pop("evaluation_id", UNSET))

        multi_turn_rerun_open_ai_finetune_request = cls(
            threshold=threshold,
            max_turns=max_turns,
            model_name=model_name,
            test_result_ids=test_result_ids,
            evaluation_id=evaluation_id,
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
