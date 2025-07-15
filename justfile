@_default:
    just --list --unsorted

# Run all build-related recipes in the justfile
run-all: install-deps format-python check-python check-spelling check-commits test

# Install the pre-commit hooks
install-precommit:
  # Install pre-commit hooks
  uvx pre-commit install
  # Run pre-commit hooks on all files
  uvx pre-commit run --all-files
  # Update versions of pre-commit hooks
  uvx pre-commit autoupdate

# Install Python package dependencies
install-deps:
  uv sync --upgrade --dev --all-extras

# Check Python code with the linter for any errors that need manual attention
check-python:
  uv run ruff check .

# Reformat Python code to match coding style and general structure
format-python:
  uv run ruff check --fix .
  uv run ruff format .

# Run checks on commits with non-main branches
check-commits:
  #!/bin/zsh
  branch_name=$(git rev-parse --abbrev-ref HEAD)
  number_of_commits=$(git rev-list --count HEAD ^$branch_name)
  if [[ ${branch_name} != "main" && ${number_of_commits} -gt 0 ]]
  then
    uv run cz check --rev-range main..HEAD
  else
    echo "Not on main or haven't committed yet."
  fi

# Check for spelling errors in files
check-spelling:
  uv run typos

test:
  #!/bin/zsh
  temp_dir="_temp/test-data-package"
  rm -rf $temp_dir
  mkdir -p $temp_dir
  # vcs-ref means the current commit/head, not a tag.
  # `.` means the current directory contains the template.
  uvx copier copy --vcs-ref=HEAD . $temp_dir \
    --defaults \
    --data package_abbrev= "test-data-package" \
    --data package_github="first-last/test-data-package" \
    --data author_given_name="First" \
    --data author_family_name="Last" \
    --data author_email="first.last@example.com"
  # TODO: Other checks/tests?

cleanup:
  #!/bin/zsh
  temp_dir=$("_temp/test-data-package"))
  rm -rf $temp_dir
