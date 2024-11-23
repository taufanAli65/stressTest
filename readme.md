# Stress Test Tool with Login Authentication

This tool is designed to perform a stress test on a target server by sending a high volume of requests in a controlled manner. It supports login functionality and uses asynchronous requests for efficient stress testing.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [Login](#login)
  - [Stress Test](#stress-test)

## Overview

This script performs the following tasks:
1. **Login** to the target URL using a POST request with a username and password.
2. **Stress Test** the target server by sending a specified number of GET requests, with a limit on how many requests can be sent per second.

The tool uses:
- **`requests`** for the login functionality (synchronous).
- **`aiohttp`** for the asynchronous stress test (non-blocking).
- **`asyncio`** to manage concurrent tasks and handle multiple requests efficiently.

## Prerequisites

- Python 3.x
- The following Python libraries must be installed:
  - `requests`
  - `aiohttp`

To install the required libraries, run the following:

```bash
pip install requests aiohttp
```

## Setup and Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/taufanAli65/stressTest.git
    ```
2. Navigate to the project directory:
    ```sh
    cd stressTest
    ```
## Usage

### Login

Before performing the stress test, you need to log in to the target server. Update the `config.json` file with your login credentials and target URL.

### Stress Test

To run the stress test, execute the `main.py` script with the desired parameters:
```bash
python main.py
```
