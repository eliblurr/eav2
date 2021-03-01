"""Add a column

Revision ID: 2ccb57b9e467
Revises: 998f1ffe52a5
Create Date: 2021-03-01 11:48:10.267555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ccb57b9e467'
down_revision = '998f1ffe52a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
