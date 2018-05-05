"""Inception

Revision ID: 5ec35fb7cfe3
Revises: 
Create Date: 2018-05-01 16:08:03.568657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ec35fb7cfe3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cache',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('uuid', sa.String(length=40), nullable=False),
    sa.Column('registered_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False),
    sa.Column('level', sa.SmallInteger(), nullable=False),
    sa.Column('activation_token', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('email'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('characters',
    sa.Column('owner', sa.String(length=40), nullable=False),
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('owner_hash', sa.String(length=50), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('characters')
    op.drop_table('users')
    op.drop_table('cache')
    # ### end Alembic commands ###