[![Lean Action CI](https://github.com/inaciovasquez2020/scientific-infrastructure/actions/workflows/lean_action_ci.yml/badge.svg)](https://github.com/inaciovasquez2020/scientific-infrastructure/actions/workflows/lean_action_ci.yml)

# scientific-infrastructure

**Canonical environment, deployment, and reproducibility layer for the Vasquez Research ecosystem.**

This repository defines the unified computational infrastructure used across all Universal Reference Frame (URF)–aligned research modules. It serves as the *single source of truth* for environment configuration, dependency locking, and execution guarantees within the Vasquez Index.

---

## Purpose and Scope

The `scientific-infrastructure` repository provides the **operational substrate** required to build, verify, and reproduce results from URF-based research projects, including but not limited to:

- `urf-core`
- `chronos-urf-rr`
- `radiative-rigidity`
- `biological-friction-framework`
- other Vasquez Index–registered modules

All computational claims published under the Vasquez Index are validated against the environments specified here.

---

## What This Repository Provides

- **Environment orchestration**
  - Canonical container and dependency specifications
  - Stable execution context for Lean, LaTeX, Python, and verification tooling

- **Reproducibility guarantees**
  - Versioned infrastructure states
  - Backward compatibility with archived results

- **CI / automation backbone**
  - Continuous integration templates
  - Deterministic build and verification pipelines

This repository is **infrastructure only**. It contains no scientific claims, axioms, or domain logic.

---

## Minimal Directory Map

This repository intentionally maintains a small, explicit surface area.

---

## Canonical Registry Status

This repository is a registered infrastructure module of the **Vasquez Index**.

- **Dashboard:**  
  https://inaciovasquez2020.github.io/vasquez-index/dashboard.html

Operational status, environment hashes, and compatibility notes are maintained there.

---

## Related Canonical Modules

### URF Prefab System
- **Repository:** https://github.com/inaciovasquez2020/urf-prefab-system  
- **Role:** Executable prefab layer (axioms, schemas, verifiers, integrity manifests)  
- **Status:** Frozen — v1.0.0  
- **Dependency:** URF Core (locked)

The prefab system consumes the infrastructure defined here.

---

## Repository Metadata

- **Repository:** `inaciovasquez2020/scientific-infrastructure`
- **Role:** Environment Orchestration & Reproducibility
- **Status:** Operational
- **Change Policy:** Versioned, backward-compatible updates only

---

## Usage Notes

- This repository should be **cloned or referenced first** when running or reproducing any URF-aligned research module.
- All downstream repositories implicitly depend on the environment guarantees defined here.
- Infrastructure updates are intentionally conservative and explicitly versioned.

---

## Citation

If you use this repository to reproduce results or deploy URF-related frameworks, please cite:

```bibtex
@manual{Vasquez_Scientific_Infrastructure_2026,
  author = {Vasquez, Inacio F.},
  title  = {scientific-infrastructure: Unified Research Environment and Deployment},
  year   = {2026},
  url    = {https://github.com/inaciovasquez2020/scientific-infrastructure}
}
