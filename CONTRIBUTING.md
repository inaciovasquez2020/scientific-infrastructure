# Contributing to Scientific Infrastructure

This repository is the canonical reproducibility, provenance, CI, manifests, and verification layer for the URF ecosystem.

## Contribution classes

### 1. Documentation improvements

- clarify onboarding wording
- improve navigation across infrastructure surfaces
- tighten quickstart and setup text
- fix broken or ambiguous references

### 2. Verification and reproducibility hardening

- improve infrastructure checks
- tighten manifest-facing validation
- strengthen reproducibility documentation
- harden status/dependency consistency

### 3. Scope or authority changes

These require explicit justification.

- changing canonical infrastructure-role language
- changing compatibility or status boundaries
- expanding authority claims
- altering infrastructure-only scope declarations

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run repository checks before commit:

```bash
./scripts/infra check
python3 -m pytest -q
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- changing infrastructure-authority language without synchronized documentation updates
- expanding scope or status claims without updating the manifest and status surfaces
