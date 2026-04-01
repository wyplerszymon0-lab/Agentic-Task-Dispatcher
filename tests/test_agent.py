import pytest
from src.agent_logic import TaskRouter

def test_router_math():
    router = TaskRouter()
    decision = '{"tool": "calculator", "input": "2+2"}'
    assert "Result of 2+2 is 4" in router.resolve(decision)

def test_router_invalid_json():
    router = TaskRouter()
    assert router.resolve("not a json") == "Error parsing agent decision."
