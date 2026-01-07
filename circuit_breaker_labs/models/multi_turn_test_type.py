from enum import Enum


class MultiTurnTestType(str, Enum):
    SEMANTIC_CHUNKS = "semantic_chunks"
    USER_PERSONA = "user_persona"

    def __str__(self) -> str:
        return str(self.value)
