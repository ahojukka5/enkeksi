# Releasing

## One-time PyPI setup

Configure a GitHub Actions Trusted Publisher on the existing PyPI project:

- **Owner:** `ahojukka5`
- **Repository:** `enkeksi`
- **Workflow:** `publish.yml`
- **Environment:** `pypi`

The publisher is added from the PyPI project's **Manage → Publishing** page.
No API token or password is stored in GitHub. The workflow receives a
short-lived OIDC credential only while the publishing job runs.

## Release checklist

1. Update the version in `pyproject.toml` with `uv version`.
2. Update `CHANGELOG.md` and documentation.
3. Run all quality gates:

   ```console
   uv sync --all-groups
   uv run ruff format --check .
   uv run ruff check .
   uv run mypy
   uv run pytest
   uv build
   uv run --group docs mkdocs build --strict
   ```

4. Merge the release pull request after CI succeeds.
5. Create and push an annotated `v<version>` tag and create a GitHub Release.
6. Confirm that the `Publish release to PyPI` workflow builds and smoke-tests
   both the wheel and source distribution before upload.
7. Verify the published version on PyPI and install it in a clean environment.

The publishing workflow can also be started manually with **Run workflow**.
This is useful when a tag was created before Trusted Publishing was configured.
