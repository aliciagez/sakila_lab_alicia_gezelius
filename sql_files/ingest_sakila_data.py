import dlt 
from dlt.sources.sql_database import sql_database
from pathlib import Path 

path_sakila_data = Path(__file__).parent[1] / "sakila" 
sqlite_path = path_sakila_data / "sqlite-sakila.db"
duckdb_path = path_sakila_data / "sakila.duckdb"

source = sql_database(f"sqlite:///{sqlite_path}", schema="main")

pipline = dlt.pipeline(
    pipeline_name="sakila_duckdb",
    destination=dlt.destinations.duckdb(str(duckdb_path)),
    dataset_name="staging"
)

load_database = pipline.run(source, write_disposition="replace")