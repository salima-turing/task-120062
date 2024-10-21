
from behave import given, when, then
import pandas as pd

@given('two datasets for merging')
def step_impl(context):
	context.left_data = pd.DataFrame({
		"id": [1, 2, 3],
		"name": ["Alice", "Bob", "Charlie"]
	})

	context.right_data = pd.DataFrame({
		"id": [3, 4, 5],
		"age": [25, 30, 35]
	})

@when('we merge the datasets on the "id" column')
def step_impl(context):
	context.merged_data = context.left_data.merge(context.right_data, on="id", how="outer")

@then('the merged dataset should contain the correct columns')
def step_impl(context):
	expected_columns = ["id", "name", "age"]
	assert list(context.merged_data.columns) == expected_columns, f"Columns mismatch. Expected: {expected_columns}, Actual: {list(context.merged_data.columns)}"

@then('the merged dataset should have the valid data')
def step_impl(context):
	expected_data = pd.DataFrame({
		"id": [1, 2, 3, 4, 5],
		"name": ["Alice", "Bob", "Charlie", None, None],
		"age": [None, None, 25, 30, 35]
	})
	pd.testing.assert_frame_equal(context.merged_data.fillna(None), expected_data, check_dtype=False)
