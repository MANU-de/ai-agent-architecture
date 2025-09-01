
# This component simulates how an agent receives input.

def get_user_input():
    """
    Simulates the perception system by capturing a user's request.
    In a real-world scenario, this could come from a chat interface,
    voice command, or sensor data.
    """
    print("Perception: Listening for input...")
    user_request = input("USER: ")
    return user_request

if __name__ == '__main__':
    request = get_user_input()
    print(f"\nAgent perceived the following request: '{request}'")
