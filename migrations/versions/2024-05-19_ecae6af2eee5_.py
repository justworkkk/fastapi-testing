"""empty message

Revision ID: ecae6af2eee5
Revises: 403e49c408bb
Create Date: 2024-05-19 17:38:33.144283

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "ecae6af2eee5"
down_revision: Union[str, None] = "403e49c408bb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("role")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("role_id", sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.create_foreign_key("user_role_id_fkey", "user", "role", ["role_id"], ["id"])
    op.create_table(
        "role",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "permission",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="role_pkey"),
    )
    # ### end Alembic commands ###
