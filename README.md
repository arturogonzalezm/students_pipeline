# Students Pipeline

### Instructions:

- Open up your command line tool and pull the SQL Server Docker image:
```python
sudo docker pull mcr.microsoft.com/mssql/server:2019-latest
```
- Launch container:
```python
docker run -d --name sql_server_demo -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=reallyStrongPwd123' -p 1433:1433 mcr.microsoft.com/mssql/server:2019-latest
```
- To extract, normalise and load the data to the db please run the main.py file.
