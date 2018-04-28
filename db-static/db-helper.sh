#!/bin/bash
# vim:ts=4
#
# Handle static data required by Bootini Star, namely EVE Online
# item groups and item types.

dbname="$1"
shift

TABLES='groups types'
case "$1" in
	dump)
		opt='--clean --column-inserts'
		for table in $TABLES; do
			pg_dump $opt --table=$table $dbname | bzip2 >$t.sql.bz2
		done
		;;
	load)
		for table in $TABLES; do
			bzcat $table.sql.bz2 | psql --quiet $dbname
		done
		;;
	*)
		echo "Usage: $(basename $0) {dbname} {dump | load}" >&2
		exit 1
esac
