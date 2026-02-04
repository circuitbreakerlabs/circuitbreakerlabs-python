from enum import Enum


class TestCaseGroup(str, Enum):
    SUICIDAL_IDEATION = "suicidal_ideation"

    def __str__(self) -> str:
        return str(self.value)
