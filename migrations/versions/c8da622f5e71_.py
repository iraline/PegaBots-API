"""empty message

Revision ID: c8da622f5e71
Revises: 
Create Date: 2021-10-14 12:26:45.668709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8da622f5e71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('handle', sa.String(length=80), nullable=False),
    sa.Column('total', sa.String(length=120), nullable=True),
    sa.Column('network', sa.String(length=120), nullable=True),
    sa.Column('sentiment', sa.String(length=120), nullable=True),
    sa.Column('friends', sa.String(length=120), nullable=True),
    sa.Column('temporal', sa.String(length=120), nullable=True),
    sa.Column('twitter_id', sa.String(length=120), nullable=True),
    sa.Column('twitter_handle', sa.String(length=120), nullable=True),
    sa.Column('twitter_user_name', sa.String(length=120), nullable=True),
    sa.Column('twitter_is_protected', sa.Boolean(), nullable=True),
    sa.Column('twitter_user_description', sa.String(length=255), nullable=True),
    sa.Column('twitter_followers_unt', sa.Integer(), nullable=True),
    sa.Column('twitter_friends_count', sa.Integer(), nullable=True),
    sa.Column('twitter_location', sa.String(length=120), nullable=True),
    sa.Column('twitter_is_verified', sa.TIMESTAMP(timezone=120), nullable=True),
    sa.Column('twitter_lang', sa.TIMESTAMP(timezone=120), nullable=True),
    sa.Column('twitter_default_profile', sa.String(length=255), nullable=True),
    sa.Column('twitter_profile_image', sa.String(length=255), nullable=True),
    sa.Column('twitter_withheld_in_countries', sa.String(length=255), nullable=True),
    sa.Column('cache_times_served', sa.Integer(), nullable=True),
    sa.Column('cache_validity', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feedbacks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('analisis_id', sa.String(length=80), nullable=False),
    sa.Column('feedback', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relatorios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('report_name', sa.String(), nullable=False),
    sa.Column('analise_id', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relatorios')
    op.drop_table('feedbacks')
    op.drop_table('analises')
    # ### end Alembic commands ###
