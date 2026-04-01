import os
from openai import OpenAI
from src.agent_logic import TaskRouter
from src.prompt_templates import AgentPrompts
from dotenv import load_dotenv

load_dotenv()

def run_agent_demo():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    router = TaskRouter()
    
    user_query = "Calculate 152 * 43 + 12"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": AgentPrompts.SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )
    
    llm_decision = response.choices[0].message.content
    print(f"🤖 LLM Decision: {llm_decision}")
    
    final_output = router.resolve(llm_decision)
    print(f"⚙️ Execution Result: {final_output}")

if __name__ == "__main__":
    run_agent_demo()
