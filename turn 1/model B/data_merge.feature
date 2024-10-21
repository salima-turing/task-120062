
### Feature file: data_merge.feature
```features
Feature: Validate Data Merge Operation

  Scenario: Merge two datasets and verify validity
    Given two input datasets are prepared
    When we merge the datasets on "id" column
    Then the merged dataset should contain the correct number of records
    And the merged dataset should have valid values
    And the names of all employees should be present
