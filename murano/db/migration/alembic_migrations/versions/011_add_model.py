revision = '011'
down_revision = '010'

import uuid

from alembic import op
from oslo_utils import timeutils
import sqlalchemy as sa
from sqlalchemy.sql.expression import table as sa_table

from murano.common import consts
from murano.db.sqla import types as st


MYSQL_ENGINE = 'InnoDB'
MYSQL_CHARSET = 'utf8'

def upgrade():
    op.create_table(
        'model',
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.Column('id', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('tenant_id', sa.String(length=36), nullable=False),
        sa.Column('version', sa.BigInteger(), nullable=False),
        sa.Column('type', sa.Integer(), nullable=False),
        sa.Column('model', sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('tenant_id', 'name'),
        mysql_engine=MYSQL_ENGINE,
        mysql_charset=MYSQL_CHARSET
    )

def downgrade():
    op.drop_table('model')
