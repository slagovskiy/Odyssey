"""empty message

Revision ID: ee9b39b6b37b
Revises: c77adb22f953
Create Date: 2016-02-08 13:29:20.549587

"""

# revision identifiers, used by Alembic.
revision = 'ee9b39b6b37b'
down_revision = 'c77adb22f953'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_categories',
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['blog_category.category_id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['blog_post.post_id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_categories')
    ### end Alembic commands ###