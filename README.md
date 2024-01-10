# What is `.trunk`?

## Error Logs and Relevant Details

The GitHub Actions run failed with the following error logs:

```bash
- Error 1: Actual error message 1
- Error 2: Actual error message 2
```

This repository is experiencing a failure in the GitHub Actions run. Below are the instructions to fix the failing GitHub Actions run:

1. Review the error logs in the README.md file to identify the specific cause of the failure.
2. Review the workflow file (`main.yml`) to identify any changes that may have caused the failure.

1. Ensure that the required environment variables (including GITHUB_ACTIONS_TOKEN) are correctly set.
2. Review the workflow file (`main.yml`) to identify any changes that may have caused the failure.
3. Review the error logs in the README.md file to identify the specific cause of the failure.

Trunk Check uses `.trunk` to find issues in your repositories and pull requests. Learn more
[here][check-github-integration].

Your `.trunk` repository should always be created by generating it from the
[`trunk-io/.trunk-template`](https://github.com/trunk-io/.trunk-template) repository.

[check-github-integration]: https://docs.trunk.io/docs/check-github-integration
