import pytest
from dotenv import load_dotenv
from app import app

def pytest_runtest_setup(item):
    print("Setting up test: ", item)
    load_dotenv()

