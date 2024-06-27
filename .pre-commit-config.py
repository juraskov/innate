default_language_version:
    # all hooks should run with python 3.6+
    python: python3
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: no-commit-to-branch
      - id: check-executables-have-shebangs
      - id: check-shebang-scripts-are-executable
      - id: check-added-large-files
        args: ['--maxkb=500', '--enforce-all']
      - id: check-yaml
      - id: check-toml

  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.2.1
    hooks:
#      - id: ruff
#        args: [--show-source, --fix]
#      - id: ruff-format
