"""add foreing-key to the posts table

Revision ID: 55039a6c448d
Revises: 98c7a204cdf3
Create Date: 2023-03-15 07:35:13.891055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55039a6c448d'
down_revision = '98c7a204cdf3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
                          local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass
