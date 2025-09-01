
# This component simulates the agent's memory.

class AgentMemory:
    """
    A simple memory system for the AI agent.
    - Short-term memory holds recent interactions.
    - Long-term memory stores key facts and learned knowledge.
    """
    def __init__(self):
        self.short_term_memory = []
        self.long_term_memory = {}
        print("Memory: Initialized.")

    def add_to_short_term(self, data):
        """Adds a new interaction to the short-term memory."""
        print(f"Memory: Adding '{data}' to short-term memory.")
        self.short_term_memory.append(data)

    def add_to_long_term(self, key, value):
        """Stores a piece of information in the long-term knowledge base."""
        print(f"Memory: Storing '{key}: {value}' in long-term memory.")
        self.long_term_memory[key] = value

    def get_context(self):
        """Retrieves the current context from memory."""
        return {
            "conversation_history": self.short_term_memory,
            "knowledge": self.long_term_memory
        }

if __name__ == '__main__':
    memory = AgentMemory()
    memory.add_to_short_term("User said: Hello!")
    memory.add_to_long_term("User's name", "Alex")
    context = memory.get_context()
    print(f"\nRetrieved context: {context}")