# create Postgresql database connection
username = 'username'
password = 'password'
db_name = 'db_name'
table_name = 'table_name'

host = 'subdomain.domain.com'
engine = create_engine('postgresql+psycopg2://' + username + ':' + password + '@' + host + ':5433/' + db_name, use_batch_mode = True)

query = """ select * from db_name.table_name  """

master_df = pd.read_sql(query, engine)
