import pprint
import logging

# set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__file__)

# set up pretty printer
pretty_printer = pprint.PrettyPrinter(indent=2, sort_dicts=False)
def log_pretty(obj):
    """Pretty print an object."""
    return f'{pretty_printer.pformat(obj)}\n'


def add_unique(item, target_list, seen_set):
    """Helper function to add unique items to a list and track in a set."""
    if item not in seen_set:
        target_list.append(item)
        seen_set.add(item)

def extract_option_values(option_prefix, all_parts, part_index):
    """Extracts values associated with a given option prefix from a command line.
    
    Args:
        option_prefix (str): The option prefix to look for (e.g., '-I', '-L').
        all_parts (list[str]): List of all parts of the command line.
        part_index (int): Index of the current part.
        
    Returns:
        str: Value associated with the specified option prefix.
    """
    # Split the command respecting quoted strings
    value = None 
    
    # handle the case where part_index is more than size of all_parts
    if part_index >= len(all_parts):
        return None
    
    part = all_parts[part_index]
    if part.startswith(option_prefix):
        # Case 1: Option and value are combined, e.g., -I"/path with spaces"
        if part != option_prefix:
            value = part[len(option_prefix):]  # Extract the value after the prefix
        
        # Case 2: Option and value are separate, e.g., -I "/path with spaces"
        elif part_index + 1 < len(all_parts):
            value = all_parts[part_index + 1]
    
    return value

def format_for_cmake(value):
    """Format a value for use in a CMake command."""
    value = value.replace('"', '\\"')  # Escape inner quotes
    return f'"{value}"' if ' ' in value else value
