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

from utils import format_for_cmake

def generate_cmake_content(build_data):
    """
    Generates the content for a CMakeLists.txt file based on parsed build data.
    
    Args:
        build_data (dict): A dictionary containing extracted compiler and linker options.
        
    Returns:
        str: A string containing the generated CMakeLists.txt content.
    """
    cmake_lines = []
    
    #Variables to be used in the generated CMakeLists.txt file
    project_name = "MyProject"
    executable_name = "MyExecutable"

    # Project name (you can customize this)
    cmake_lines.append("cmake_minimum_required(VERSION 3.10)\n")
    cmake_lines.append(f"project({project_name})\n\n")
    
        # Add sources directories
    if build_data["sources"]:
        cmake_lines.append("set(SOURCES\n")
        for source in build_data["sources"]:
            cmake_lines.append(f"    {format_for_cmake(source)}\n")
        cmake_lines.append(")\n\n")

    # Add executable, and add sources to it
    cmake_lines.append(f"add_executable({executable_name} {'${SOURCES}'})\n\n")

    # Add include directories
    if build_data["include_dirs"]:
        cmake_lines.append(f"target_include_directories({executable_name} PRIVATE\n")
        for include in build_data["include_dirs"]:
            cmake_lines.append(f"    {format_for_cmake(include)}\n")
        cmake_lines.append(")\n\n")

    # Add compiler flags
    if build_data["compiler_flags"]:
        cmake_lines.append(f"target_compile_options({executable_name} PRIVATE\n")
        for flag in build_data["compiler_flags"]:
            cmake_lines.append(f"    {format_for_cmake(flag)}\n")
        cmake_lines.append(")\n\n")

    # Add linker directories
    if build_data["library_dirs"]:
        cmake_lines.append(f"target_link_directories({executable_name} PRIVATE\n")
        for link in build_data["library_dirs"]:
            cmake_lines.append(f"    {format_for_cmake(link)}\n")
        cmake_lines.append(")\n\n")

    # Add libraries
    if build_data["libraries"]:
        cmake_lines.append(f"target_link_libraries({executable_name} PRIVATE\n")
        for library in build_data["libraries"]:
            cmake_lines.append(f"    {format_for_cmake(library)}\n")
        cmake_lines.append(")\n\n")


    return ''.join(cmake_lines)
