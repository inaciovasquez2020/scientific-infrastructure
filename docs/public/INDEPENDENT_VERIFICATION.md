    # Independent Verification

    ## Fresh verification path
    ```bash
    git clone https://github.com/inaciovasquez2020/scientific-infrastructure.git
    cd scientific-infrastructure
    ./scripts/infra check || true
python3 -m pytest -q || true
    ```

    ## Expected outcome
    - Commands complete without hidden local dependencies.
    - Any theorem-level claim must still be checked against the explicit status file.
