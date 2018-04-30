"""Activation token

Revision ID: b561d52833d8
Revises: 697f73f79c02
Create Date: 2018-04-30 23:00:49.051340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b561d52833d8'
down_revision = '697f73f79c02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('activation_token', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'activation_token')
    # ### end Alembic commands ###
