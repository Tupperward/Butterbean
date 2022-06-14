#!/usr/bin/env sh

STATUS=0

echo "postgresql-backup-restore: restore: Started"

# Ensure the database user exists.
echo "postgresql-backup-restore: checking for DB user ${DB_USER}"
result=$(psql --host=${DB_HOST} --username=${DB_USER} --command='\du' | grep ${DB_USER})
if [ -z "${result}" ]; then
    result=$(psql --host=${DB_HOST} --username=${DB_USER} --command="create role ${DB_USER} with login password '${DB_PASS}' inherit;")
    if [ "${result}" != "CREATE ROLE" ]; then
        message="Create role command failed: ${result}"
        echo "postgresql-backup-restore: FATAL: ${message}"
        exit 1
    fi
fi

# Delete database if it exists.
echo "postgresql-backup-restore: checking for DB ${DB_NAME}"
result=$(psql --host=${DB_HOST} --username=${DB_USER} --list | grep ${DB_NAME})
if [ -z "${result}" ]; then
    message="Database "${DB_NAME}" on host "${DB_HOST}" does not exist."
    echo "postgresql-backup-restore: INFO: ${message}"
else
    echo "postgresql-backup-restore: deleting database ${DB_NAME}"
    result=$(psql --host=${DB_HOST} --dbname=postgres --username=${DB_USER} --command="DROP DATABASE ${DB_NAME};")
    if [ "${result}" != "DROP DATABASE" ]; then
        message="Create database command failed: ${result}"
        echo "postgresql-backup-restore: FATAL: ${message}"
        exit 1
    fi
fi

echo "postgresql-backup-restore: restoring ${DB_NAME}"
start=$(date +%s)
psql --host=${DB_HOST} --username=${DB_USER} --dbname=postgres ${DB_OPTIONS}  < /tmp/${DB_NAME}.sql || STATUS=$?
end=$(date +%s)

if [ $STATUS -ne 0 ]; then
    echo "postgresql-backup-restore: FATAL: Restore of ${DB_NAME} returned non-zero status ($STATUS) in $(expr ${end} - ${start}) seconds."
    exit $STATUS
else
    echo "postgresql-backup-restore: Restore of ${DB_NAME} completed in $(expr ${end} - ${start}) seconds."
fi

echo "postgresql-backup-restore: restore: Completed"
exit $STATUS