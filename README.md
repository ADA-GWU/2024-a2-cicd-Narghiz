# Wikipedia Selenium Test Suite

This is a Selenium test suite designed to automate testing on Wikipedia's website. It consists of three test cases:

1. *Test Wikipedia Title*: Verifies if the title of the Wikipedia homepage contains the expected keyword "Wikipedia".
2. *Test Search Functionality*: Validates the search functionality by searching for the term "Python programming language" and checking if the search results page contains relevant content.
3. *Test Footer Links*: Ensures that all links in the footer section of Wikipedia's homepage point to pages within Wikipedia's domain.

## Prerequisites

Before running the tests, ensure that you have the following installed:

- Python 3.x
- Selenium WebDriver for Chrome (make sure the chromedriver is in your PATH)

## Setup

1. Clone this repository to your local machine

2. Install the required Python packages using pip:

    bash
    pip install selenium
    

3. Download the appropriate chromedriver for your Chrome version and place it in a directory that is included in your system's PATH.

## Running the Tests

To execute the test suite, navigate to the project directory in your terminal and run:

```bash
python main.py
