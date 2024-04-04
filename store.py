from datetime import datetime
import databases
import sqlalchemy as sql

DATABASE_URL = "sqlite:///store.db"

database = databases.Database(DATABASE_URL)
metadata = sql.MetaData()

users = sql.Table(
    "users",
    metadata,
    sql.Column("id", sql.Integer, primary_key=True),
    sql.Column("first_name", sql.String(40)),
    sql.Column("last_name", sql.String(80)),
    sql.Column("email", sql.String(120)),
    sql.Column("password", sql.String(40)),
)

products = sql.Table(
    "products",
    metadata,
    sql.Column("id", sql.Integer, primary_key=True),
    sql.Column("title", sql.String(80)),
    sql.Column("description", sql.String(512)),
    sql.Column("price", sql.Float),
)

orders = sql.Table(
    "orders",
    metadata,
    sql.Column("id", sql.Integer, primary_key=True),
    sql.Column("date", sql.String(64), nullable=False, default=datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
              onupdate=datetime.now().strftime("%d/%m/%y, %H:%M:%S")),
    sql.Column("status", sql.String(8), nullable=False, server_default="Создан"),
    sql.Column("user_id", sql.Integer, sql.ForeignKey('users.id'), nullable=False),
    sql.Column("product_id", sql.Integer, sql.ForeignKey('products.id'), nullable=False),
)

engine = sql.create_engine(DATABASE_URL)

metadata.create_all(engine)