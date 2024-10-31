"""
src/cmake_generator.py

This module provides a function to generate the content for a CMakeLists.txt
file based on parsed build data extracted from build logs. The generated CMake
configuration includes compiler flags, linker flags, include directories, and
libraries, facilitating the creation of CMake projects from existing build logs.

Function:
- generate_cmake_content(build_data): Generates a CMakeLists.txt content
  string from the provided build data.
"""

def generate_cmake_content(build_data):
    """
    Generates the content for a CMakeLists.txt file based on parsed build data.
    
    Args:
        build_data (dict): A dictionary containing extracted compiler and linker options.
        
    Returns:
        str: A string containing the generated CMakeLists.txt content.
    """
    cmake_lines = []

    # Project name (you can customize this)
    cmake_lines.append("cmake_minimum_required(VERSION 3.10)\n")
    cmake_lines.append("project(MyProject)\n\n")

    # Add include directories
    if build_data["include_dirs"]:
        cmake_lines.append("include_directories(\n")
        for include in build_data["include_dirs"]:
            cmake_lines.append(f"    {include}\n")
        cmake_lines.append(")\n\n")

    # Add compiler flags
    if build_data["compiler_flags"]:
        cmake_lines.append("add_compile_options(\n")
        for flag in build_data["compiler_flags"]:
            cmake_lines.append(f"    {flag}\n")
        cmake_lines.append(")\n\n")

    # Linker flags and libraries
    if build_data["linker_flags"]:
        cmake_lines.append("link_directories(\n")
        for link in build_data["linker_flags"]:
            cmake_lines.append(f"    {link}\n")
        cmake_lines.append(")\n\n")

    if build_data["libraries"]:
        cmake_lines.append("target_link_libraries(MyExecutable\n")  # Assuming a target name
        for library in build_data["libraries"]:
            cmake_lines.append(f"    {library}\n")
        cmake_lines.append(")\n\n")

    # Adding a simple executable target (customize target name as needed)
    cmake_lines.append("add_executable(MyExecutable main.cpp)  # Replace with your source files\n")

    return ''.join(cmake_lines)
