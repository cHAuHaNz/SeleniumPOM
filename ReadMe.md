# Selenium Automation Project with Python using Page Object Model (POM)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This repository contains a Selenium automation project with Python, designed to provide a structured foundation for web testing. The project includes setup instructions, configuration management, and base files for building test cases.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
    - [Dependencies](#dependencies)
    - [Configuration](#configuration)
- [Base Functionality](#base-functionality)
    - [Setup and Teardown](#setup-and-teardown)
    - [BaseTest](#basetest)
    - [BasePage](#basepage)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is organized into the following packages:

- `config`: Contains configuration files, such as `config.ini`.
- `tests`: Houses test cases and the `conftest.py` file for setup and teardown.
- `pages`: Includes page classes, with a `BasePage` class for common functionality.
- `reports`: Reserved for storing test reports.

## Setup

### Dependencies

Before running the project, ensure you have the necessary dependencies installed. Use the following steps:

1. Install VS Code or an Integrated Development Environment (IDE) like PyCharm or IntelliJ IDEA.
2. Open this project in the IDE or VS Code.
3. Install the required packages listed in `requirements.txt` by running the following command in terminal:
   ```bash
   pip3 install -r requirements.txt
    ```
4. Install the latest version of [ChromeDriver](https://chromedriver.chromium.org/downloads) and add it to your PATH.

### Configuration

The project uses a configuration file, `config.ini`, to store environment-specific settings. The file is located in the `config` package. The following settings are available:

- `base_url`: The base URL for the application under test.
- `browser`: The browser to use for testing. The default is Chrome.
- `timeout`: The default timeout for waiting for elements to load. The default is 10 seconds.

## Base Functionality

The project includes base classes for setting up and running tests, as well as a base page class for common functionality.

### Setup and Teardown

The `conftest.py` file in the `tests` package contains setup and teardown methods for the test suite. The `setup` method is run before each test case, and the `teardown` method is run after each test case. The methods are used to initialize the driver and navigate to the base URL before each test case, and to close the driver after each test case.

### BaseTest

The `BaseTest` class in the `tests` package is the parent class for all test cases. It applies the `setup_and_teardown` fixture from `conftest.py` to each test case, and provides the `driver` object for interacting with the browser.

### BasePage

The `BasePage` class in the `pages` package is the parent class for all page classes. It provides common functionality for interacting with the browser, such as clicking elements, entering text, and waiting for elements to load.

## Usage

To run the test suite, use the following command in terminal:

```bash
pytest
```

To run a specific test case, use the following command in terminal:

```bash
pytest tests/HomeTest.py
```

## Contributing

Contributions are welcome! To contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to the new branch.
5. Submit a pull request.
6. Wait for your pull request to be reviewed and merged.
7. Celebrate! 🎉

## License

This project is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) license.
