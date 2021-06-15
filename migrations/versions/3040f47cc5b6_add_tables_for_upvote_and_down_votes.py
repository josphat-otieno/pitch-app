"""add tables for upvote and down votes

Revision ID: 3040f47cc5b6
Revises: 9c858f63072b
Create Date: 2021-06-15 15:56:22.207135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3040f47cc5b6'
down_revision = '9c858f63072b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('downvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('downvote', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('upvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upvote', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('comments', 'comment',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('pitches', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('pitches', 'post_pitch',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('users', 'password_secure',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password_secure',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('pitches', 'post_pitch',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('pitches', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('comments', 'comment',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_table('upvotes')
    op.drop_table('downvotes')
    # ### end Alembic commands ###
