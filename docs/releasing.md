# Releasing

## One-time PyPI setup

Before the first upload, configure a pending GitHub Actions Trusted Publisher
for the new `sqlfence` project on PyPI:

- **Owner:** `ahojukka5`
- **Repository:** `sqlfence`
- **Workflow:** `publish.yml`
- **Environment:** `pypi`

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
6. Confirm that `Publish release to PyPI` smoke-tests both distributions before upload.
7. Verify the published version and install it in a clean environment.

The publishing workflow also supports **Run workflow**, which is useful after
configuring a pending Trusted Publisher.
