# autoware-interface-check

This command checks the following.

- autoware-parameter-schema

## Usage

The following steps are required to run the test:

1. Create a test suite file such as [example/test/autoware_guideline_check.yaml](../example/test/autoware_guideline_check.yaml).
2. Add export tag such as [example/package.xml](../example/package.xml).
3. Run the check command in the workspace containing the above package.

## Command

```bash
autoware-guideline-check
```

| Options      | Type   | Description                                              |
| ------------ | ------ | -------------------------------------------------------- |
| --workspaces | string | List of workspace root paths.                            |
| --xunit-file | string | File path of xUnit. This is for colcon test integration. |
| --xunit-name | string | Test name of xUnit. This is for colcon test integration. |

## Example

```txt
$ autoware-guideline-check --workspace example
Test #0 (Success)
  message: OK
  details:
    schema: example/schema/foo.schema.json
    params: example/config/foo_success.param.yaml

Test #1 (Failure)
  message: 'frame' is a required property
  details:
    schema: example/schema/foo.schema.json
    params: example/config/foo_failure.param.yaml

Summary
  all    : 2
  success: 1
  failure: 1
  errors : 0
```
