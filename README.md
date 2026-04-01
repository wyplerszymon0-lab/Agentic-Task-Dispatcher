* Orchestra-AI: Agentic Task Dispatcher 
A robust orchestration layer for LLMs that enables structured tool-use through a deterministic routing engine.

* The Problem: Unreliable Agent Behavior
Standard LLM agents often fail when transitioning from "conversation" to "execution". They might hallucinate tool names, provide malformed arguments, or trigger the wrong functions, leading to system instability.

* The Solution: JSON-Enforced Orchestration
Orchestra-AI acts as a Dispatcher. It forces the LLM to function as a decision-maker that outputs strictly formatted instructions, which are then executed by a safe, isolated Python environment.

* Key Architecture
Strict Schema Enforcement: The agent is prompted to respond only with valid JSON, ensuring machine-readable commands.

Tool Registry: A centralized dispatcher (TaskRouter) maps LLM decisions to real Python functions (calculators, DB connectors, etc.).

Safe Execution Loop: Separates the "thinking" (LLM) from the "doing" (code), preventing common prompt injection or execution errors.

* Implemented Tools
Calculator: Real-time evaluation of mathematical expressions.

Database Connector: Mocked interface for structured data retrieval.

Web Search Router: Logic for handling external information requests.

* Technical Stack
Python: Core dispatch logic.

OpenAI API: Used as the "reasoning engine" (GPT-4o).

JSON Schema: For output validation.

Pytest: Validating router logic and error handling.

* Usage
Configure your environment variables and run the dispatcher:

* Python
from src.agent_logic import TaskRouter

# Dispatch a user request through the logic engine
router = TaskRouter()
decision = '{"tool": "calculator", "input": "152 * 43"}'
result = router.resolve(decision)
