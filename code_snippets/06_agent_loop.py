
# A final script to simulate the entire agentic loop.

from o1_perception import get_user_input
from o2_memory import AgentMemory
from o3_reasoning_engine import reasoning_engine
from o4_planning import create_plan
from o5_action import execute_action

def run_agent():
    """Simulates a full conversation loop."""
    # 1. Initialize the agent's memory
    memory = AgentMemory()

    # 2. Start the interaction loop
    while True:
        # PERCEPTION
        user_request = get_user_input()
        if user_request.lower() == 'exit':
            print("Agent: Goodbye!")
            break
        
        memory.add_to_short_term(f"User: {user_request}")

        # REASONING
        context = memory.get_context()
        decision = reasoning_engine(user_request, context)
        memory.add_to_short_term(f"Agent Thought: {decision}")

        # PLANNING
        plan = create_plan(decision)
        
        # ACTION
        for step in plan:
            result = execute_action(step, memory)
            # Feedback Loop: The result of an action can inform the next one.
            # In this simple model, we just print the final response.
            if step['action'] == 'respond':
                # Here, we could dynamically insert the tool result into the message.
                # For simplicity, we're just printing.
                print(f"AGENT: {step['message']}")

        print("-" * 20)

if __name__ == '__main__':
    run_agent()