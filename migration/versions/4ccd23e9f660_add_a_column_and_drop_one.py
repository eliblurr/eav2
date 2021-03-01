"""Add a column and drop one

Revision ID: 4ccd23e9f660
Revises: 2ccb57b9e467
Create Date: 2021-03-01 11:49:55.369611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ccd23e9f660'
down_revision = '2ccb57b9e467'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('new', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')
