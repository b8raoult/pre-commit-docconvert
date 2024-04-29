# docconvert pre-commit hook

A pre-commit hook to check that Python docstrings are following one
of the standard convention.

Usage:

```yaml
- repo: https://github.com/b8raoult/pre-commit-docconvert
  rev: "0.1.4"
  hooks:
  - id: docconvert
    args: ["numpy"]
```

`args` can be `google`, `numpy`, `rest` or `epytext`.

See https://github.com/cbillingham/docconvert for more information.
