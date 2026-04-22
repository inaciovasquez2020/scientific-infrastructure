# Scientific Infrastructure Quickstart

This is the shortest path from clone to a first successful local verification pass.

## Requirements

- `git`
- `bash`
- `python3`

## 1. Clone

```bash
git clone https://github.com/inaciovasquez2020/scientific-infrastructure.git
cd scientific-infrastructure
```

## 2. Check tools

```bash
python3 --version
git --version
```

## 3. Run the canonical infrastructure check

```bash
./scripts/infra check
```

## 4. Review the main infrastructure surfaces

- `README.md`
- `STATUS.md`
- `MANIFEST.md`
- `DEPENDENCIES.md`
- `docs/`

## 5. Next steps

- detailed setup: `docs/SETUP_GUIDE.md`
- contribution policy: `CONTRIBUTING.md`
