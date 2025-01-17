"""create_users_table

Revision ID: ffdc0a98111c
Revises:
Create Date: 2020-11-20 15:06:02.230689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffdc0a98111c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('balance', sa.Float(2), default=10000),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    op.create_table('lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('stocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(100), nullable=False),
    sa.Column('ticker', sa.String(5), nullable=False),
    sa.Column('price', sa.Float(2), nullable=False),
    sa.Column('description', sa.String(length=2200), nullable=False),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('ticker'),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('stockid', sa.Integer(), nullable=False),
    sa.Column('shares', sa.Float(2), nullable=False),
    sa.Column('share_value', sa.Float(2), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.ForeignKeyConstraint(['stockid'], ['stocks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('list_stocks',
    sa.Column('listid', sa.Integer()),
    sa.Column('stockid', sa.Integer()),
    sa.ForeignKeyConstraint(['listid'], ['lists.id'], ),
    sa.ForeignKeyConstraint(['stockid'], ['stocks.id'], )
    )


    # ### end Alembic commands ###qqqqqqqqq


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('list_stocks')
    op.drop_table('transactions')
    op.drop_table('lists')
    op.drop_table('stocks')
    op.drop_table('users')
    # ### end Alembic commands ###
