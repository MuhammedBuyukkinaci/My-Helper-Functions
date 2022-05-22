import pytest

@pytest.fixture
def my_fixture():
    return 51


@pytest.fixture
def captured_print(capsys):
    print("hello")

# Pass this fixture to test_demo via argument.
@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Muhammed",
            "family_name": "Buyukkinaci",
            "title": "Data Scientist",
        },
        {
            "given_name": "Ahmet",
            "family_name": "Kaya",
            "title": "Project Manager",
        },
    ]