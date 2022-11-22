"""Campo tipo drake removido

Revision ID: d9aab1aef720
Revises: 4d4c6414eb63
Create Date: 2022-06-13 21:11:27.389961

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d9aab1aef720"
down_revision = "4d4c6414eb63"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_column("matchup_map", "first_drake_type")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "matchup_map",
        sa.Column("first_drake_type", sa.NullType(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###