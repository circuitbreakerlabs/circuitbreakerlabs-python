from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SingleTurnEvaluateOpenAiFinetuneRequest")


@_attrs_define
class SingleTurnEvaluateOpenAiFinetuneRequest:
    """
    Attributes:
        threshold (float): Responses below this safety score threshold will fail
        variations (int): Number of variations per unsafe case
        maximum_iteration_layers (int): Maximum iteration layers for tests
        test_case_groups (list[str]): One or more test case groups to run
        model_name (str): Fully qualified name of the model to be tested.
    """

    threshold: float
    variations: int
    maximum_iteration_layers: int
    test_case_groups: list[str]
    model_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold = self.threshold

        variations = self.variations

        maximum_iteration_layers = self.maximum_iteration_layers

        test_case_groups = self.test_case_groups

        model_name = self.model_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "threshold": threshold,
                "variations": variations,
                "maximum_iteration_layers": maximum_iteration_layers,
                "test_case_groups": test_case_groups,
                "model_name": model_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        threshold = d.pop("threshold")

        variations = d.pop("variations")

        maximum_iteration_layers = d.pop("maximum_iteration_layers")

        test_case_groups = cast(list[str], d.pop("test_case_groups"))

        model_name = d.pop("model_name")

        single_turn_evaluate_open_ai_finetune_request = cls(
            threshold=threshold,
            variations=variations,
            maximum_iteration_layers=maximum_iteration_layers,
            test_case_groups=test_case_groups,
            model_name=model_name,
        )

        single_turn_evaluate_open_ai_finetune_request.additional_properties = d
        return single_turn_evaluate_open_ai_finetune_request

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
