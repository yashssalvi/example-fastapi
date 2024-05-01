"""add foreign-key to post table

Revision ID: 0b3b68c3b968
Revises: 53ac194c0bd4
Create Date: 2024-04-30 19:17:17.426734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b3b68c3b968'
down_revision: Union[str, None] = '53ac194c0bd4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
