"""add insurance and regional_area

Revision ID: 6c4135d06295
Revises: 2386a184b3da
Create Date: 2026-06-18 10:34:34.261480

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


revision: str = '6c4135d06295'
down_revision: Union[str, None] = '2386a184b3da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.add_column(
        "orders",
        sa.Column("insurance", sa.Float(), nullable=True)
    )

    op.add_column(
        "orders",
        sa.Column("regional_area", sa.String(100), nullable=True)
    )

def downgrade():
    op.drop_column("orders", "regional_area")
    op.drop_column("orders", "insurance")