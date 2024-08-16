## Commit Messages Convention
We follow the Default Commits specification by commitlint package to ensure a consistent and informative commit history. This helps us automate the release process and make it easier to understand the purpose of each change.

### Commit Message Structure
Each commit message should consist of a type, an optional scope, and a subject:

```vim
<type>(<scope>): <subject>
```
* `type`: A keyword that describes the purpose of the commit (e.g., feat, fix, docs, refactor).
* `scope`: An optional keyword that provides additional context about what part of the codebase is affected (e.g., auth, api, ui).
* `subject`: A brief description of the changes made.
### Common Types
* **feat**: Adding a new feature.
* **fix**: Fixing a bug.
* **docs**: Documentation changes.
* **style**: Code style changes (formatting, white-space, etc.).
* **refactor**: Code improvements without adding features or fixing bugs.
* **test**: Adding or updating tests.
* **build**: Changes to the build system or dependencies.
* **ci**: Changes to CI configuration files or scripts.
* **chore**: Maintenance tasks, such as updating dependencies or scripts.
* **revert**: Reverting a previous commit.

Please follow [commitlint](https://github.com/conventional-changelog/commitlint) package for detailed information.
_____

<br/>

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
