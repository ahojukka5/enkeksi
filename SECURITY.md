# Security policy

## Supported versions

Security fixes are provided for the latest stable release.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability. Use GitHub's private
security advisory reporting for this repository.

`enkeksi` executes SQL contained in input documents. Treat Markdown files as
executable input, use read-only databases whenever possible, and review files
before running with `--write`.
