"""hash pass user

Revision ID: e24eefb81e98
Revises: 5503d97b7eea
Create Date: 2021-12-30 12:29:52.043971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e24eefb81e98"
down_revision = "5503d97b7eea"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("hashed_pass", sa.String(length=256), nullable=False)
    )
    op.create_unique_constraint(None, "users", ["hashed_pass"])
    op.drop_column("users", "verified")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("verified", sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    op.drop_constraint(None, "users", type_="unique")
    op.drop_column("users", "hashed_pass")
    # ### end Alembic commands ###
