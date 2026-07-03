from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleTurnRerunSystemPromptRequest")


@_attrs_define
class SingleTurnRerunSystemPromptRequest:
    """
    Attributes:
        threshold (float):
        variations (int):
        maximum_iteration_layers (int):
        system_prompt (str):
        openrouter_model_name (str):
        test_result_ids (list[int] | None | Unset):
        evaluation_id (int | None | Unset):
    """

    threshold: float
    variations: int
    maximum_iteration_layers: int
    system_prompt: str
    openrouter_model_name: str
    test_result_ids: list[int] | None | Unset = UNSET
    evaluation_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold = self.threshold

        variations = self.variations

        maximum_iteration_layers = self.maximum_iteration_layers

        system_prompt = self.system_prompt

        openrouter_model_name = self.openrouter_model_name

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
                "variations": variations,
                "maximum_iteration_layers": maximum_iteration_layers,
                "system_prompt": system_prompt,
                "openrouter_model_name": openrouter_model_name,
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

        variations = d.pop("variations")

        maximum_iteration_layers = d.pop("maximum_iteration_layers")

        system_prompt = d.pop("system_prompt")

        openrouter_model_name = d.pop("openrouter_model_name")

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

        single_turn_rerun_system_prompt_request = cls(
            threshold=threshold,
            variations=variations,
            maximum_iteration_layers=maximum_iteration_layers,
            system_prompt=system_prompt,
            openrouter_model_name=openrouter_model_name,
            test_result_ids=test_result_ids,
            evaluation_id=evaluation_id,
        )

        single_turn_rerun_system_prompt_request.additional_properties = d
        return single_turn_rerun_system_prompt_request

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
