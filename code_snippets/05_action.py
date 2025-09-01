
# This component simulates the agent taking action.

# --- Mock Tools the Agent Can Use ---
def tool_weather_api(query):
    """A fake tool that "checks" the weather."""
    return "Sunny with a high of 25°C"

def tool_add_to_memory(memory_system, key, value):
    """A fake tool that adds info to memory."""
    memory_system.add_to_long_term(key, value)
    return "Information stored."
# ------------------------------------

def execute_action(step, memory):
    """
    Executes a single step from the plan.
    This involves using tools or formulating a response.
    """
    action = step.get("action")
    print(f"\nAction: Executing '{action}'...")

    if action == "use_tool":
        tool_name = step.get("tool")
        if tool_name == "weather_api":
            result = tool_weather_api(step.get("query"))
            print(f"Action: Used weather tool, got result -> '{result}'")
            return result
        # Can add more tools here...
    elif action == "add_to_memory":
        result = tool_add_to_memory(memory, step.get("key"), step.get("value"))
        return result
    elif action == "respond":
        message = step.get("message")
        print(f"Action: Responding to user -> '{message}'")
        return message
    else:
        print("Action: Unknown action.")
        return None

if __name__ == '__main__':
    from o2_memory import AgentMemory # Import to use memory
    mock_memory = AgentMemory()
    mock_plan_step = {"action": "use_tool", "tool": "weather_api", "query": "current weather"}
    execute_action(mock_plan_step, mock_memory)