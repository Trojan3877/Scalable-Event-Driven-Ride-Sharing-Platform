# Developer Dependencies

This project uses [pip-tools](https://github.com/jazzband/pip-tools) to keep
dev dependencies reproducible.

| File | Purpose |
|------|---------|
| `requirements-dev.txt` | Human-maintained input: list of top-level dev packages |
| `requirements-dev.lock` | Auto-generated lock file with pinned versions **and SHA-256 hashes** |

---

## Prerequisites

Install pip-tools once into your virtual environment:

```bash
python -m pip install pip-tools
```

---

## Compiling the lock file

Re-generate `requirements-dev.lock` from `requirements-dev.txt`:

```bash
make lock-dev
# equivalent: pip-compile --generate-hashes requirements-dev.txt --output-file requirements-dev.lock
```

Commit the updated `requirements-dev.lock` along with any changes to
`requirements-dev.txt`.

---

## Installing / syncing from the lock file

Install the exact locked versions (removes any packages not in the lock file):

```bash
make sync-dev
# equivalent: pip-sync requirements-dev.lock
```

---

## Updating dependencies (minor/patch)

To pull in the latest compatible minor/patch releases:

```bash
pip-compile --upgrade --generate-hashes requirements-dev.txt --output-file requirements-dev.lock
```

Or upgrade a single package (e.g. `pytest`):

```bash
pip-compile --upgrade-package pytest --generate-hashes requirements-dev.txt --output-file requirements-dev.lock
```

After compiling, sync your environment:

```bash
make sync-dev
```

Then commit both `requirements-dev.txt` (if changed) and `requirements-dev.lock`.
