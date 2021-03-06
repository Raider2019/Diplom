"""Many to many

Revision ID: 58d03f21d141
Revises: c30373766efe
Create Date: 2022-03-21 20:21:30.593347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58d03f21d141'
down_revision = 'c30373766efe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id_orders', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('cargo', sa.String(length=150), nullable=True),
    sa.Column('weight', sa.String(length=60), nullable=True),
    sa.Column('check_orders', sa.String(length=50), nullable=True),
    sa.Column('ts_orders', sa.DateTime(), nullable=True),
    sa.Column('city_sender', sa.Integer(), nullable=True),
    sa.Column('steet_sender', sa.String(length=255), nullable=True),
    sa.Column('house_number', sa.Integer(), nullable=True),
    sa.Column('date_senders', sa.String(length=60), nullable=True),
    sa.Column('date_recipients', sa.String(length=60), nullable=True),
    sa.Column('pay_method', sa.String(length=60), nullable=True),
    sa.Column('suma', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['city_sender'], ['citys.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_users'], ),
    sa.PrimaryKeyConstraint('id_orders')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###
