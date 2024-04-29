# docconvert pre-commit hook

A pre-commit hook to check that Python docstrings are following one
of the standard convention.

Usage:

```yaml
- repo: https://github.com/b8raoult/pre-commit-docconvert
  rev: "0.1.3"
  hooks:
  - id: docconvert
    args: ["--in-place", "--output", "numpy"]
```

`args` can be `google`, `numpy`, `rest` or `epytext`.

See https://github.com/cbillingham/docconvert for more information.
