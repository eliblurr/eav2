"""create account table

Revision ID: 998f1ffe52a5
Revises: 
Create Date: 2021-03-01 11:38:33.240974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '998f1ffe52a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
