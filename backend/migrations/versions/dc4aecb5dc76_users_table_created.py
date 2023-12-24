"""Users table created!

Revision ID: dc4aecb5dc76
Revises: 
Create Date: 2023-11-07 21:07:57.075169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc4aecb5dc76'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('password', sa.String),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade() -> None:
    op.drop_table('users')
