@_default:
    just --list --unsorted

# Run all build-related recipes in the justfile
run-all: install-deps format-python check-python check-commits

# Install Python package dependencies
install-deps:
  uv sync --upgrade --dev

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
