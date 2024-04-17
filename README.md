# logging-extended-handlers

[![PyPI - Version](https://img.shields.io/pypi/v/logging-extended-handlers.svg)](https://pypi.org/project/logging-extended-handlers)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/logging-extended-handlers.svg)](https://pypi.org/project/logging-extended-handlers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

-----

**Table of Contents**

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## About

This package contains the following loggers:

- `HTTPHandlerCustomHeader`: Like `logging.handlers.HTTPHandler` but with full freedom of the HTTP header
- `BufferingSMTPHandler`: Buffers the logs like `logging.handlers.BufferingHandler` and sends it via smtp

## Installation

```console
pip install logging-extended-handlers
```

## Usage

Eg.

```python
logger = logging.getLogger()
logger.setLevel("DEBUG")
my_logger = MyLogger(...)
my_logger.setLevel("INFO")
my_formatter = logging.Formatter(
    fmt="%(asctime)s %(levelname)s by %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    style="%",
)
my_logger.setFormatter(my_formatter)
logger.addHandler(my_logger)
```

## License

`logging-extended-handlers` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
