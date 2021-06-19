"""change description

Revision ID: 4654f7488d1c
Revises: 5f69b19b9071
Create Date: 2021-06-17 16:02:05.085565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4654f7488d1c'
down_revision = '5f69b19b9071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('description', sa.Text(), nullable=True))
    op.drop_column('pitches', 'descrption')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('descrption', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'description')
    # ### end Alembic commands ###