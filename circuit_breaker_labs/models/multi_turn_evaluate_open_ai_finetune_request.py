from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.multi_turn_test_type import MultiTurnTestType
from ..models.test_case_pack import TestCasePack
from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiTurnEvaluateOpenAiFinetuneRequest")


@_attrs_define
class MultiTurnEvaluateOpenAiFinetuneRequest:
    """
    Attributes:
        threshold (float): Responses below this safety score threshold will fail
        max_turns (int): Maximum number of turns in the conversation. Should be a multiple of two.
        test_types (list[MultiTurnTestType]): One or more multi-turn-test types
        model_name (str): Fully qualified name of the model to be tested.
        test_case_packs (list[TestCasePack] | Unset): One or more test case packs to run. Defaults to suicidal ideation
            tests
    """

    threshold: float
    max_turns: int
    test_types: list[MultiTurnTestType]
    model_name: str
    test_case_packs: list[TestCasePack] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold = self.threshold

        max_turns = self.max_turns

        test_types = []
        for test_types_item_data in self.test_types:
            test_types_item = test_types_item_data.value
            test_types.append(test_types_item)

        model_name = self.model_name

        test_case_packs: list[str] | Unset = UNSET
        if not isinstance(self.test_case_packs, Unset):
            test_case_packs = []
            for test_case_packs_item_data in self.test_case_packs:
                test_case_packs_item = test_case_packs_item_data.value
                test_case_packs.append(test_case_packs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "threshold": threshold,
                "max_turns": max_turns,
                "test_types": test_types,
                "model_name": model_name,
            }
        )
        if test_case_packs is not UNSET:
            field_dict["test_case_packs"] = test_case_packs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        threshold = d.pop("threshold")

        max_turns = d.pop("max_turns")

        test_types = []
        _test_types = d.pop("test_types")
        for test_types_item_data in _test_types:
            test_types_item = MultiTurnTestType(test_types_item_data)

            test_types.append(test_types_item)

        model_name = d.pop("model_name")

        _test_case_packs = d.pop("test_case_packs", UNSET)
        test_case_packs: list[TestCasePack] | Unset = UNSET
        if _test_case_packs is not UNSET:
            test_case_packs = []
            for test_case_packs_item_data in _test_case_packs:
                test_case_packs_item = TestCasePack(test_case_packs_item_data)

                test_case_packs.append(test_case_packs_item)

        multi_turn_evaluate_open_ai_finetune_request = cls(
            threshold=threshold,
            max_turns=max_turns,
            test_types=test_types,
            model_name=model_name,
            test_case_packs=test_case_packs,
        )

        multi_turn_evaluate_open_ai_finetune_request.additional_properties = d
        return multi_turn_evaluate_open_ai_finetune_request

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
