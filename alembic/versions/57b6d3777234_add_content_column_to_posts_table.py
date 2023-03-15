"""add content column to posts table

Revision ID: 57b6d3777234
Revises: b9fed4a3a9db
Create Date: 2023-03-14 23:41:37.227536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57b6d3777234'
down_revision = 'b9fed4a3a9db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
