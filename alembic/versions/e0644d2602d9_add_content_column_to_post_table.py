"""add content column to post table

Revision ID: e0644d2602d9
Revises: d51e6b0d3259
Create Date: 2024-04-30 18:51:13.365166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0644d2602d9'
down_revision: Union[str, None] = 'd51e6b0d3259'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:    
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
