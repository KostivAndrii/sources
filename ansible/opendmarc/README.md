experimental opendmarc with PostgreSQL support

Build with

./configure --with-sql-backend=Pg --with-spf

psql -h localhost -d opendmarc -U opendmarc -f /etc/opendmarc/import.sql --set ON_ERROR_STOP=1

/usr/sbin/opendmarc-reports --dbhost=${DB_SERVER} --dbuser=${DB_USER} --dbpasswd=${DB_PASS} --dbname=${DB_NAME} --verbose --interval=86400 --report-email $REPORT_EMAIL --report-org 'base48.cz'
/usr/sbin/opendmarc-import --dbhost=${DB_SERVER} --dbuser=${DB_USER} --dbpasswd=${DB_PASS} --dbname=${DB_NAME} --verbose < ${WORK_DIR}/opendmarc_import.dat
