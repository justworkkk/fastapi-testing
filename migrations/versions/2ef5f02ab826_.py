"""empty message

Revision ID: 2ef5f02ab826
Revises: 81ed6ef0366f
Create Date: 2024-05-23 17:59:24.048986

"""

from typing import Sequence, Union
from src.config import DB_NAME
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2ef5f02ab826"
down_revision: Union[str, None] = "81ed6ef0366f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "operation",
        "date",
        existing_type=sa.TIMESTAMP(),
        type_=sa.DateTime(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "operation",
        "date",
        existing_type=sa.DateTime(),
        type_=sa.TIMESTAMP(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###
