import json

class TaskRouter:
    def __init__(self):
        self.tools = {
            "calculator": self._execute_math,
            "database": self._fetch_data,
            "search": self._web_search
        }

    def _execute_math(self, query):
        return f"Result of {query} is {eval(query)}"

    def _fetch_data(self, query):
        return f"Data for {query}: [Record found]"

    def _web_search(self, query):
        return f"Search results for {query}: [Link 1, Link 2]"

    def resolve(self, llm_decision):
        try:
            decision = json.loads(llm_decision)
            tool_name = decision.get("tool")
            tool_input = decision.get("input")
            
            if tool_name in self.tools:
                return self.tools[tool_name](tool_input)
            return "No tool needed, direct response."
        except:
            return "Error parsing agent decision."
