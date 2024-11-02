"""
src/log_parser.py

This module provides functions to parse build log files and extract relevant
compiler and linker commands. It supports common formats used in various
build systems, enabling the generation of CMake configuration from build logs.

Functions:
- parse_build_log(log_file_path): Parses the specified build log file
  and returns a dictionary of extracted compiler and linker options.
- add_unique(item, target_list, seen_set): Helper function to add unique items
  to a list while tracking them in a set.
- log_pretty(obj): Helper function to pretty print objects for logging.
"""

import logging
from utils import log_pretty
from parsers import gpp_parser, msvc_parser

# set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__file__)

def parse_build_log(log_file_path):
    """
    Parses the build log to extract compiler and linker commands.
    
    Args:
        log_file_path (str): Path to the build log file.
        
    Returns:
        dict: Dictionary containing parsed compiler and linker options.
    """
    build_data = {
        "compiler_flags": [],
        "debug_flags": [],
        "linker_flags": [],
        
        "include_dirs": [],
        "library_dirs": [],
        "libraries": [],
        "output": None,
        "sources": [],
        "others": []
    }

    try:
        # Read the log file line by line
        with open(log_file_path, "r", encoding="utf-8") as log_file:
            for line in log_file:
                # Check if the line contains a known compiler and send to the appropriate function
                if "g++ " in line:
                    command = line.split("g++ ", 1)[1].strip()
                    gpp_parser.process_line(command, build_data)
                # elif "gcc" in line:
                #     command = line.split("gcc", 1)[1].strip()
                #     handle_gcc(command)
                elif "cl " in line:
                    command = line.split("cl ", 1)[1].strip()
                    msvc_parser.process_line(command, build_data)
            # logging.info("Parsed build data:\n%s", log_pretty(build_data))
    except IOError as e:
        print(f"Error reading log file {log_file_path}: {e}")
        return None

    return build_data

