"""Inception

Revision ID: 48b3a4702a28
Revises: 
Create Date: 2018-04-27 21:53:51.778413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48b3a4702a28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cache',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('uuid', sa.String(length=40), nullable=False),
    sa.Column('registered_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False),
    sa.Column('level', sa.SmallInteger(), server_default='1', nullable=False),
    sa.PrimaryKeyConstraint('email'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('characters',
    sa.Column('owner', sa.String(length=40), nullable=False),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('owner_hash', sa.String(length=50), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('types',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('groupid', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['groupid'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('types')
    op.drop_table('characters')
    op.drop_table('users')
    op.drop_table('groups')
    op.drop_table('cache')
    # ### end Alembic commands ###
