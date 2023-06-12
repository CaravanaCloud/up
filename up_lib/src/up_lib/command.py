from dataclasses import dataclass


@dataclass
class Command:
    command: tuple
    options: dict
    prompt: list

