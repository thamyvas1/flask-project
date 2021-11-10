"""empty message

Revision ID: 729b3eaf79b8
Revises: e0ecaafecfe6
Create Date: 2021-11-10 17:28:26.867293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '729b3eaf79b8'
down_revision = 'e0ecaafecfe6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owners')
    # ### end Alembic commands ###
