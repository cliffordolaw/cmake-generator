# CMake Generator

A Python tool to generate `CMakeLists.txt` files automatically from build logs. 

## Project Overview

### Objective
This tool is designed to automate the creation of `CMakeLists.txt` files from build logs of various systems. It parses compiler and linker commands, identifies necessary include paths, libraries, and flags, and generates a comprehensive `CMakeLists.txt` file that can be used across platforms.

### Features
- **Cross-platform Support**: Works with both Linux (`g++`) and Windows (`MSVC`) build environments.
- **Modular Parsing**: Separate parsers for different compiler formats (e.g., g++ and MSVC) for extensibility.
- **CMake Syntax Translation**: Automatically translates compiler and linker flags into CMake-compatible syntax.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:cliffordolaw/cmake-generator.git
   cd cmake-generator
   ```

2. **Install Dependencies**: Use pip to install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 

1. **Prepare Your Build Log**: Obtain a build log from your existing build process. For example:

```bash
make > build_log.txt  # For Linux systems
```

2. **Run the Tool**: Execute the main script, passing in your build log file:

```bash
    python3 src/main.py --log examples/sample_build.log --output examples/generated_CMakeLists.txt
```

3. **Output**: The tool will generate a `CMakeLists.txt` file based on the parsed log, ready for use in your project.

## Project Structure

1. **Directory Structure**:
    ```
    cmake-automation-tool/
    ├── src/
    │   ├── main.py             # Entry point for the CMake Generator tool
    │   ├── cmake_generator.py  # Generates CMake syntax from parsed data
    │   ├── log_parser.py       # Extracts compiler and linker commands from logs
    │   └── parsers/            # Contains individual parsers for g++, MSVC, etc.
    ├── tests/                  # Unit tests and sample build logs for validation
    ├── examples/               # Example logs and output CMakeLists.txt files
    ├── README.md               # Project documentation
    ├── CONTRIBUTING.md         # Guidelines for contributing to this project
    └── requirements.txt        # Project dependencies
    ```

## Contributing
Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For questions or suggestions, feel free to open an issue or reach out to the maintainer on GitHub.



