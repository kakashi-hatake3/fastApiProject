"""rename reservation

Revision ID: 3644de47f4b3
Revises: 2660eee2b391
Create Date: 2024-05-11 11:57:40.463631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3644de47f4b3'
down_revision: Union[str, None] = '2660eee2b391'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
