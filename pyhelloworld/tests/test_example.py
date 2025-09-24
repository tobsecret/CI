from pyhelloworld import main


def test_main():
    """
    Testing that we can access functions from the python package for testing purposes.
    """
    assert main().startswith("Hello")
