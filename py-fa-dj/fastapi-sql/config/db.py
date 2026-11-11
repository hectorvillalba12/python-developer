from sqlalchemy  import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:3704219257@localhost:3306/storedb")

meta = MetaData()

conn = create_engine()