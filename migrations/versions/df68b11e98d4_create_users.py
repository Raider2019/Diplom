"""Create Users

Revision ID: df68b11e98d4
Revises: dc932cf451a2
Create Date: 2022-02-22 15:18:37.607370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df68b11e98d4'
down_revision = 'dc932cf451a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id_users', sa.Integer(), nullable=False),
    sa.Column('pib', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('ts_registry', sa.DateTime(), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id_users')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
