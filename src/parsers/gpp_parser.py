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

import re
import shlex
from utils import add_unique, extract_option_values

# Define regex patterns for different types of flags
warning_pattern = re.compile(r'(-W\S+|/W\d)')
optimization_pattern = re.compile(r'(-O\d)')
source_pattern = re.compile(r'(\S+\.cpp)$')

# TODO: Implement these flags
debug_pattern = re.compile(r'(-g\d*|/Zi|/Z7|/DEBUG)') 
std_pattern = re.compile(r'(-std=[^ ]+|/std:[^ ]+)') 
arch_pattern = re.compile(r'(-m(32|64)|/MACHINE:(X86|X64|ARM|ARM64))')
define_pattern = re.compile(r'(-D\S+|/D\S+)')
output_pattern = re.compile(r'-o (\S+)')


# Initialize sets to track unique items
includes_seen = set()
compiler_flags_seen = set()
sources_seen = set()
others_seen = set()
library_dirs_seen = set()
libraries_seen = set()

def process_line(line, build_data): 
    """Process a line of the build log for gpp compiler."""
    # Use shlex to split the line respecting quotes
    parts = shlex.split(line)
    
    for i, part in enumerate(parts):
        # if include_match := include_pattern.match(part):
        if part.startswith("-I"):
            include_param = extract_option_values("-I", parts, i)
            add_unique(include_param, build_data['include_dirs'], includes_seen)
        elif part.startswith("-L"):
            lib_dir = extract_option_values("-L", parts, i) 
            add_unique(lib_dir, build_data['library_dirs'], library_dirs_seen)
        elif part.startswith("-l"):
            lib_name = extract_option_values("-l", parts, i)
            add_unique(lib_name, build_data['libraries'], libraries_seen)
        elif part.startswith("-Wl,"):
            # TODO: Add linker flags, and also handle -Wp, -Wa, -f, -B
            pass
        # Add compiler_flags list
        elif warning_match := warning_pattern.match(part):
            add_unique(warning_match.group(), build_data['compiler_flags'], compiler_flags_seen)
        elif optimization_match := optimization_pattern.match(part):
            add_unique(optimization_match.group(), build_data['compiler_flags'], compiler_flags_seen)

        # Add sources list
        elif source_match := source_pattern.match(part):
            add_unique(source_match.group(), build_data['sources'], sources_seen)

        # Add others list
        else:
            add_unique(part, build_data['others'], others_seen)
            
