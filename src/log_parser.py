"""
src/log_parser.py

This module provides functions to parse build log files and extract relevant
compiler and linker commands. It supports common formats used in various
build systems, enabling the generation of CMake configuration from build logs.

Functions:
- parse_build_log(log_file_path): Parses the specified build log file
  and returns a dictionary of extracted compiler and linker options.
- extract_compiler_flags(line): Extracts compiler flags from a line of log output.
- extract_include_dirs(line): Extracts include directories from a line of log output.
- extract_linker_flags(line): Extracts linker flags from a line of log output.
- extract_libraries(line): Extracts linked libraries from a line of log output.
"""

import re

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
        "linker_flags": [],
        "include_dirs": [],
        "libraries": []
    }

    try:
        with open(log_file_path, "r", encoding="utf-8") as log_file:
            for line in log_file:
                # Parse compiler flags (e.g., -Wall, -O2 for g++, /W3 for MSVC)
                if re.search(r"\b(g\+\+|clang\+\+|cl)\b", line):
                    build_data["compiler_flags"].extend(extract_compiler_flags(line))
                    build_data["include_dirs"].extend(extract_include_dirs(line))
                
                # Parse linker flags (e.g., -lfoo, -L/usr/lib for g++, /LIBPATH for MSVC)
                if re.search(r"link", line, re.IGNORECASE) or re.search(r"\.lib\b", line):
                    build_data["linker_flags"].extend(extract_linker_flags(line))
                    build_data["libraries"].extend(extract_libraries(line))

    except IOError as e:
        print(f"Error reading log file {log_file_path}: {e}")
        return None

    return build_data

def extract_compiler_flags(line):
    """Extract compiler flags from a line of log output."""
    # Regex for common compiler flags (e.g., -Wall, -O2, /W3, etc.)
    flags = re.findall(r"(-\w+|\b/W\d\b)", line)
    return flags

def extract_include_dirs(line):
    """Extract include directories from a line of log output."""
    # Regex for include directories (e.g., -I/usr/include or /Ipath\to\include)
    includes = re.findall(r"(-I\s*[\w/\\.:]+|\b/I\s*[\w/\\.:]+)", line)
    return [inc.replace("-I", "").replace("/I", "").strip() for inc in includes]

def extract_linker_flags(line):
    """Extract linker flags from a line of log output."""
    # Regex for linker flags (e.g., -L/usr/lib or /LIBPATH:path\to\libs)
    linker_flags = re.findall(r"(-L\s*[\w/\\.:]+|\b/LIBPATH:\s*[\w/\\.:]+)", line)
    return [flag.replace("-L", "").replace("/LIBPATH:", "").strip() for flag in linker_flags]

def extract_libraries(line):
    """Extract linked libraries from a line of log output."""
    # Regex for linked libraries (e.g., -lfoo or foo.lib)
    libraries = re.findall(r"(-l\w+|\b\w+\.lib\b)", line)
    return [lib.replace("-l", "").replace(".lib", "") for lib in libraries]
