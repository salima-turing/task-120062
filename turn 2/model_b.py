import pytest
from pytest_bdd import given, when, then, scenarios

# Sample data for testing
data_set1 = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

data_set2 = [
    {"id": 2, "age": 25},
    {"id": 3, "age": 30},
]

# Sample function to perform data merging
def merge_data(data1, data2, join_key="id"):
    merged_data = []
    for record1 in data1:
        for record2 in data2:
            if record1[join_key] == record2[join_key]:
                merged_data.append({**record1, **record2})
                break
    return merged_data

scenarios('''
    Merging Data Sets
        Given I have two data sets to merge
        When I merge the data sets based on the "id" key
        Then the merged data set should contain the following records
''')

@given('I have two data sets to merge')
def prepare_data_sets():
    global data_set1, data_set2

@when('I merge the data sets based on the "id" key')
def merge_the_data_sets():
    global merged_data
    merged_data = merge_data(data_set1, data_set2)

@then('the merged data set should contain the following records')
def verify_merged_data(expected_data):
    # Convert the expected data to a set for comparison
    expected_data_set = set(tuple(d.items()) for d in expected_data)
    # Convert the merged data to a set for comparison
    merged_data_set = set(tuple(d.items()) for d in merged_data)
    assert merged_data_set == expected_data_set
