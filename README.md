# What is `.trunk`?

Trunk Check uses `.trunk` to find issues in your repositories, pull requests, and GitHub Actions. Learn more
[here][check-github-integration].

Your `.trunk` repository should always be created by generating it from the [`trunk-io/.trunk-template`](https://github.com/trunk-io/.trunk-template) repository. Additionally, it is crucial to ensure that your GitHub Actions are correctly configured and running.
[`trunk-io/.trunk-template`](https://github.com/trunk-io/.trunk-template) repository.

[check-github-integration]: https://docs.trunk.io/docs/check-github-integration

## How to Fix the Failing GitHub Actions
If your GitHub Actions are failing, please follow these instructions to fix the issue:
1. Check the error logs to identify the specific cause of the failure.
2. Ensure that your workflow file is correctly configured with the required steps and dependencies.
3. Verify the environment setup and prerequisites required for the workflow.
4. Make sure that any external dependencies or services used in the workflow are functioning as expected.
5. Test the workflow locally to identify and address any issues before pushing changes to the repository.
6. If the issue persists, refer to relevant documentation and community forums for additional support and troubleshooting tips.
