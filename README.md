# emailo

[![Build Status](https://travis-ci.org/2tunnels/emailo.svg?branch=master)](https://travis-ci.org/2tunnels/emailo)
[![codecov](https://codecov.io/gh/2tunnels/emailo/branch/master/graph/badge.svg)](https://codecov.io/gh/2tunnels/emailo)

emailo is a command line tool for parsing and analyzing emails from different files.
Might be helpful for scraping and investigating dumps from breaches.

## Installation

emailo is a Python package, so I strongly recommend you to install it in separate `virtualenv`.

```sh
$ pip install emailo
```

## Parse

Parsing simple SQL dump:

```sh
$ emailo parse ~/Dumps/example.sql
john@example.com
bill@example.net
alex@example.org
troy@example.com
...
```

You can filter emails by domain using `endswith` options like so:

```sh
$ emailo parse ~/Dumps/example.sql --endswith=@example.com
john@example.com
troy@example.com
...
```

emailo will output emails in `stdout`, don't forget to save them somewhere:

```sh
$ emailo parse ~/Dumps/example.sql > emails.txt
```

## Domains

Sometimes you need to know which domains are most popular in your email list:

```sh
$ emailo domains ~/Lists/emails.txt
example.com 2
example.net 1
example.org 1
```

Or you can get percentage value:

```sh
$ emailo domains ~/Lists/emails.txt --percentage
example.com 50.00%
example.net 25.00%
example.org 25.00%
```

## New feature request

If there is a missing functionality that you need, don't hesitate to create an [issue](https://github.com/2tunnels/emailo/issues).
