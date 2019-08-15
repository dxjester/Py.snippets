
# build DB connection

username = 'your_username'
password = 'your_password'
db_name = 'database_name'
schema_name = 'schema_name'
table_name = 'table_name'

host = 'doman_name.sub_domain_name.com'
engine = create_engine('ostgresql+psycopg2://'+username+':'password+'@'+host+':9987/'+ db_name, use_batch_mode=True)

master_df = pd.read_sql_table(table_name, engine, schema = schema_name)

# retrieve all records and convert as dataframe
query = """ select * from schema_name.table_name """
master_df = pd.read_sql(query,engine)
master_df.head(10)
