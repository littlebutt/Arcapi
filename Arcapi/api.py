import abc
import functools
from typing import Any


class Api:
    @abc.abstractmethod
    def call_action(self, action: str, **params) -> Any:
        pass

    def __getattr__(self, item: str):
        return functools.partial(self.call_action, item)