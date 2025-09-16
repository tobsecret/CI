from pyhelloworld import main


def test_passes():
    """
    This test doesn't test anything and is just here so pytest
    returns a 0 exit status which requires at least 1 test to be run.
    """
    assert True


def test_main():
    """
    Testing that we can access functions from the python package for testing purposes.
    """
    assert main().startswith("Hello")
