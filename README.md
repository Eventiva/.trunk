# What is `.trunk`?

Your `.trunk` repository should always be created by generating it from the [`trunk-io/.trunk-fix`](https://github.com/trunk-io/.trunk-fix) repository. The following steps outline how to generate the `.trunk` repository and ensure its correct integration with the Trunk Check.
1. Clone the `trunk-io/.trunk-fix` repository to your local environment.
2. Make necessary changes and additions to the repository content to align with your specific requirements.
3. Push the modified `.trunk-fix` repository to your GitHub account.
4. Provide access to Trunk Check for the `.trunk` repository through the Trunk web interface or by granting appropriate permissions.
5. Verify the correct integration of the `.trunk` repository with the Trunk Check.
Issue Title: [Sweep GHA Fix]
```
// Trunk Check uses `.trunk` to find issues in your repositories and pull requests. The GitHub Actions run failed with the following error logs:
```{{ERROR_LOGS}}```
```
[here][check-github-integration].

The following steps outline how to generate the `.trunk` repository and ensure its correct integration with the Trunk Check.
1. Clone the `trunk-io/.trunk-fix` repository to your local environment.
2. Make necessary changes and additions to the repository content to align with your specific requirements.
3. Push the modified `.trunk-fix` repository to your GitHub account.
4. Provide access to Trunk Check for the `.trunk` repository through the Trunk web interface or by granting appropriate permissions.
5. Verify the correct integration of the `.trunk` repository with the Trunk Check.

[check-github-integration]: [Visit the troubleshooting guide](https://docs.trunk.io/docs/check-github-integration) for instructions on how to fix the issue
