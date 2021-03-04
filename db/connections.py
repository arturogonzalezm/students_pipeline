def connection_mysql_string():
    return "jdbc:mysql://localhost:3306/TEST?useLegacyDatetimeCode=false&serverTimezone=UTC"


def connection_mysql_properties():
    return {"user": "root", "password": "root", "driver": "com.mysql.jdbc.Driver"}


def connection_mssql_string():
    return "jdbc:sqlserver://localhost:1433;databaseName=TEST"


def connection_mssql_properties():
    return {"user": "sa", "password": "reallyStrongPwd123", "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"}
