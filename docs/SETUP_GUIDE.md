# Setup Guide

This guide is for contributors who want a reliable local environment for scientific-infrastructure.

## Prerequisites

```bash
python3 --version
git --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- POSIX shell environment

## Clone

```bash
git clone https://github.com/inaciovasquez2020/scientific-infrastructure.git
cd scientific-infrastructure
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Verification

```bash
./scripts/infra check
```

## Optional test pass

```bash
python3 -m pytest -q
```

## Recommended edit loop

```bash
git pull --ff-only origin main
./scripts/infra check
python3 -m pytest -q
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `STATUS.md`
- `MANIFEST.md`
- `DEPENDENCIES.md`
