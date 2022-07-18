from sqlalchemy import (
    create_engine, Table, column, Float, ForeignKey, Integer, String, MetaData
)


# Executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:////chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)



# making the connection
with db.connect() as connection: