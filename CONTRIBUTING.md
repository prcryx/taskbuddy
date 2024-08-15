## Branch Naming Convention

To maintain a consistent and organized codebase, please follow these branch naming conventions:

- **Main Branch:** `main`
- **Staging Branch:** `staging`
- **Development Branch:** `develop`
- **Release Branches:** `release/<version-tag>`
- **Feature Branches:** `feature/ref-id/your-branch-name`
- **Bugfix Branches:** `bugfix/ref-id/your-branch-name`
- **Hotfix Branches:** `hotfix/ref-id/your-branch-name`
- **Chore Branches:** `chore/ref-id/your-branch-name`
- **Documentation Branches:** `docs/ref-id/your-branch-name`

### Examples:
- `feature/123/user-authentication`
- `feature/no-ref/user-authentication`
- `bugfix/123/fix-login-error`
- `bugfix/no-ref/fix-login-error`
- `hotfix/123/security-patch`
- `release/v1.0.0`

### Important:
Commits will be allowed only on branches that adhere to the above naming conventions. Ensure that your branch name starts with one of the specified prefixes or is exactly `develop` or `staging`.

If your branch name does not match these conventions, your commit will be blocked by a pre-commit hook.

### How to Create a Branch

To create a new branch following the naming convention, use the following command:

```bash
git checkout -b feature/ref-id/your-branch-name
```
Replace `ref-id` with JIRA id or issue id if no id assigned start with `no-ref` and similarly replace `your-branch-name` with a meaningful name that describes the purpose of your branch.
