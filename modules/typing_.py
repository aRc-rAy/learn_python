from typing import List, Dict, Tuple, Any, Union

def get_user_input(prompt: str) -> str:
    """
    Get user input from the console.
    
    Args:
        prompt (str): The prompt to display to the user.
    
    Returns:
        str: The user's input.
    """
    return input(prompt)

# name = get_user_input("Enter your name: ")
# age = int(get_user_input("Enter your age: "))


# help(get_user_input)

# use list as hinting
def process_numbers(numbers: List[int]) -> List[int]:
    """
    Process a list of numbers and return the squared values.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A list of squared integers.
    """
    return [number ** 2 for number in numbers]

squared=process_numbers([1, 2, 3, 4, 5])

for val in squared:
    print(val, end="\t")