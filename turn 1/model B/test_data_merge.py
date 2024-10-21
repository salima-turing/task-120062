
### Step file: test_data_merge.py
```typescript
from behave import given, when, then
import pandas as pd
import numpy as np


@given('two input datasets are prepared')
def step_impl(context):
    # Prepare sample datasets
    data1 = {
        'id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'city': ['New York', 'San Francisco', 'Los Angeles', 'Boston']
    }
    data2 = {
        'id': [3, 4, 5, 6],
        'email': ['charlie@example.com', 'david@example.com', 'emma@example.com', 'frank@example.com'],
        'salary': [50000, 60000, 70000, 80000]
    }

    context.data1 = pd.DataFrame(data1)
    context.data2 = pd.DataFrame(data2)

@when('we merge the datasets on "id" column')
def step_impl(context):
    # Perform data merge
    context.merged_data = context.data1.merge(context.data2, on='id', how='outer')

@then('the merged dataset should contain the correct number of records')
def step_impl(context):
    # Check if the merged dataset has the expected number of records
    assert len(context.merged_data) == 6, "Unexpected number of records in the merged dataset"

@then('the merged dataset should have valid values')
def step_impl(context):
    # Check for missing values and ensure all values are expected types
    assert not context.merged_data.isnull().values.any(), "Merged dataset contains missing values"
    
    assert np.issubdtype(context.merged_data['id'].dtype, np.integer), "id column must be integers"
    assert np.issubdtype(context.merged_data['salary'].dtype, np.integer), "salary column must be integers"

@then('the names of all employees should be present')
def step_impl(context):
    # Check if all the names from data1 are present in the merged dataset
    expected_names = set(context.data1['name'])
    actual_names = set(context.merged_data.loc[context.merged_data['name'].notnull(), 'name'])
    assert expected_names.issubset(actual_names), "Missing employee names in the merged dataset"
