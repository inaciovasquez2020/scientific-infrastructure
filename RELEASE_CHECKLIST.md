This checklist defines the minimal conditions for any Tier A module
to be considered a valid scientific infrastructure component.
- [ ] LICENSE present (MIT)
- [ ] CITATION.cff present
- [ ] README.md contains:
  - Scope
  - Status
  - Releases
  - Reproducibility
  - Root Manifest backlink
- [ ] At least one annotated git tag (vX.Y)
- [ ] Clean build or execution instructions
- [ ] No untracked or experimental theory
- [ ] MANIFEST.md lists all Tier A modules
- [ ] README.md defines:
  - purpose
  - citation
  - operating rules
- [ ] RELEASE_CHECKLIST.md present
- [ ] Root tagged release exists
- [ ] Zenodo DOI minted (when applicable)
For each Tier A module:

1. Freeze release (git tag)
2. Create GitHub release
3. Mint DOI (Zenodo)
4. Submit to journal (if applicable)
5. Record DOI and journal reference in README

No step is optional.
