from sqlalchemy import create_engine
engine = create_engine('sqlite:///chatserver.db', convert_unicode=True)