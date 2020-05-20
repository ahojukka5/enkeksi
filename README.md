# enkeksi - Markdown-SQL evaluator

[![Python CI][ci-img]][ci-url]
[![Coverate Status][coveralls-img]][coveralls-url]

Package author: Jukka Aho (@ahojukka5, ahojukka5@gmail.com)

enkeksi takes a markdown-formatted input and executes the sql queries found in
it, and returns a markdown-formatted output where the results of the sql queries
have been added. Package can be used, for example, to create a dynamic project
documentation where SQL queries are automatically executed to get example
results in a dynamic manner. This way it is easy to spot from the non-working
documentation is there is problems with the database.

enkeksi comes with a command line tool `markdown-sql-eval` which can be used
to process markdown files efficiently.

Project is hosted in GitHub: <https://github.com/ahojukka5/mdeval>.

[ci-img]: https://github.com/ahojukka5/enkeksi/workflows/Python%20CI/badge.svg
[ci-url]: https://github.com/ahojukka5/enkeksi/actions
[coveralls-img]: https://coveralls.io/repos/github/ahojukka5/enkeksi/badge.svg?branch=master
[coveralls-url]: https://coveralls.io/github/ahojukka5/enkeksi?branch=master
