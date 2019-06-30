"""empty message

Revision ID: 17409e57b0d5
Revises: 
Create Date: 2019-06-30 02:24:04.632250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17409e57b0d5'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.Text(), nullable=True),
    sa.Column('date', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Session'))
    )
    op.create_index('identifier', 'Session', ['identifier'], unique=True, mysql_length=255)
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('identifier', table_name='Session')
    op.drop_table('Session')
    # ### end Alembic commands ###
