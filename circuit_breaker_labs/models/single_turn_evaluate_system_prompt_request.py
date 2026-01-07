from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_case_pack import TestCasePack
from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleTurnEvaluateSystemPromptRequest")


@_attrs_define
class SingleTurnEvaluateSystemPromptRequest:
    """
    Attributes:
        threshold (float): Responses below this safety score threshold will fail
        variations (int): Number of variations per unsafe case
        maximum_iteration_layers (int): Maximum iteration layers for tests
        system_prompt (str): The system prompt to be evaluated
        openrouter_model_name (str): Name of the model to be tested. Available models can be found at [Openrouter
            Models](https://openrouter.ai/models)
        test_case_packs (list[TestCasePack] | Unset): One or more test case packs to run. Defaults to suicidal ideation
            tests
    """

    threshold: float
    variations: int
    maximum_iteration_layers: int
    system_prompt: str
    openrouter_model_name: str
    test_case_packs: list[TestCasePack] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold = self.threshold

        variations = self.variations

        maximum_iteration_layers = self.maximum_iteration_layers

        system_prompt = self.system_prompt

        openrouter_model_name = self.openrouter_model_name

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
                "variations": variations,
                "maximum_iteration_layers": maximum_iteration_layers,
                "system_prompt": system_prompt,
                "openrouter_model_name": openrouter_model_name,
            }
        )
        if test_case_packs is not UNSET:
            field_dict["test_case_packs"] = test_case_packs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        threshold = d.pop("threshold")

        variations = d.pop("variations")

        maximum_iteration_layers = d.pop("maximum_iteration_layers")

        system_prompt = d.pop("system_prompt")

        openrouter_model_name = d.pop("openrouter_model_name")

        _test_case_packs = d.pop("test_case_packs", UNSET)
        test_case_packs: list[TestCasePack] | Unset = UNSET
        if _test_case_packs is not UNSET:
            test_case_packs = []
            for test_case_packs_item_data in _test_case_packs:
                test_case_packs_item = TestCasePack(test_case_packs_item_data)

                test_case_packs.append(test_case_packs_item)

        single_turn_evaluate_system_prompt_request = cls(
            threshold=threshold,
            variations=variations,
            maximum_iteration_layers=maximum_iteration_layers,
            system_prompt=system_prompt,
            openrouter_model_name=openrouter_model_name,
            test_case_packs=test_case_packs,
        )

        single_turn_evaluate_system_prompt_request.additional_properties = d
        return single_turn_evaluate_system_prompt_request

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
