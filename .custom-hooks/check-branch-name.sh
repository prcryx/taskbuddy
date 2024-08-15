# .custom-hooks/check-branch-name.sh
#!/bin/bash

BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)
echo "Branch Name: $BRANCH_NAME"

# Regular expression for valid primary categories
PRIMARY_REGEX="^(develop|staging|main|release/v[0-9]+\.[0-9]+\.[0-9]+)$"

# Regular expression for valid secondary categories
SECONDARY_REGEX="^(feature|bugfix|hotfix|docs|chore)/(no-ref|[A-Za-z0-9-]+)/"

# Additional checks
INVALID_CHARS_REGEX="[[:space:][:cntrl:]~^:?*\\\[@{}]"
CONSECUTIVE_DOTS_REGEX="\.\."
ENDS_WITH_DOT_OR_LOCK_REGEX="\.$|\.lock$"
BEGINS_OR_ENDS_WITH_DOT_REGEX="^\.$|^\.|[.]$"

if [[ "$BRANCH_NAME" =~ $PRIMARY_REGEX ]]; then
    echo "Branch name is valid"
elif [[ "$BRANCH_NAME" =~ $SECONDARY_REGEX ]]; then
    if [[ "$BRANCH_NAME" =~ $INVALID_CHARS_REGEX ]]; then
        echo "Branch name contains invalid characters."
        exit 1
    elif [[ "$BRANCH_NAME" =~ $CONSECUTIVE_DOTS_REGEX ]]; then
        echo "Branch name contains consecutive dots."
        exit 1
    elif [[ "$BRANCH_NAME" =~ $ENDS_WITH_DOT_OR_LOCK_REGEX ]]; then
        echo "Branch name ends with a dot or .lock."
        exit 1
    elif [[ "$BRANCH_NAME" =~ $BEGINS_OR_ENDS_WITH_DOT_REGEX ]]; then
        echo "Branch name begins or ends with a dot."
        exit 1
    else
        echo "Branch name is valid."
    fi
else
    echo "Error: Branch name does not follow the naming convention."
    echo "Branch names should start with 'feature/.../', 'bugfix/.../', 'hotfix/.../, docs/.../, chore/.../, release/ 'etc."
    echo "Please check CONTRIBUTING.md for detailed info"
    exit 1
fi
