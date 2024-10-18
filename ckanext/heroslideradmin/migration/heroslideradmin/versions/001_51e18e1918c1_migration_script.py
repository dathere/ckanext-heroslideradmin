"""Migration script

Revision ID: 51e18e1918c1
Revises: 
Create Date: 2024-09-20 11:05:11.352987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51e18e1918c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    engine = op.get_bind()
    inspector = sa.inspect(engine)
    tables = inspector.get_table_names()
    if 'hero_slider' not in tables:
        op.create_table(
            'hero_slider',
            sa.Column('id', sa.String, primary_key=True),
            sa.Column('image_url_1', sa.String),
            sa.Column('hero_text_1', sa.String),
            sa.Column('image_url_2', sa.String),
            sa.Column('hero_text_2', sa.String),
            sa.Column('image_url_3', sa.String),
            sa.Column('hero_text_3', sa.String),
            sa.Column('image_url_4', sa.String),
            sa.Column('hero_text_4', sa.String),
            sa.Column('image_url_5', sa.String),
            sa.Column('hero_text_5', sa.String),
            sa.Column('created', sa.DateTime),
            sa.Column('modified', sa.DateTime),
        )


def downgrade():
    op.drop_table('hero_slider')
