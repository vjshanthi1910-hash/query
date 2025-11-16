import oracledb

# Enable Thick mode
oracledb.init_oracle_client(lib_dir=r"C:\instantclient_23_8")

DB_USER = "HR"
DB_PASSWORD = "hr"
DB_DSN = "localhost:1521/XE"

def get_connection():
    return oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_DSN
    )
