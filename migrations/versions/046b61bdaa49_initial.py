"""initial

Revision ID: 046b61bdaa49
Revises: 
Create Date: 2023-03-29 09:36:29.287822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '046b61bdaa49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('tg_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profiles_id'), 'profiles', ['id'], unique=True)
    op.create_index(op.f('ix_profiles_tg_id'), 'profiles', ['tg_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_profiles_tg_id'), table_name='profiles')
    op.drop_index(op.f('ix_profiles_id'), table_name='profiles')
    op.drop_table('profiles')
    # ### end Alembic commands ###
