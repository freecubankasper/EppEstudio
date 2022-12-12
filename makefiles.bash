#!/bin/sh
cd data/db
mkdir -p pg_commit_ts
mkdir -p pg_tblspc
mkdir -p pg_dynshmem
mkdir -p pg_logical/mappings
mkdir -p pg_logical/snapshots
mkdir -p pg_notify
mkdir -p pg_replslot
mkdir -p pg_serial
mkdir -p pg_snapshots
mkdir -p pg_stat
mkdir -p pg_tblspc
mkdir -p pg_twophase
mkdir -p pg_wal/archive_status
echo "Restarting db_postgres container..."
docker restart eppestudio_db_postgres_1	
sleep 2
echo "Done!"
sleep 2

