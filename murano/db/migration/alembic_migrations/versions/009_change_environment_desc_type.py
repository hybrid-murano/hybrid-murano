# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Change type of description field in package table.

Revision ID: 004
Revises: table package

"""

# revision identifiers, used by Alembic.
revision = '009'
down_revision = '008'

from alembic import op
import sqlalchemy as sa

import murano.db.migration.helpers as helpers
from murano.db.sqla import types as st

MYSQL_ENGINE = 'InnoDB'
MYSQL_CHARSET = 'utf8'


def upgrade():
    engine = op.get_bind()
    engine.execute('SET FOREIGN_KEY_CHECKS=0')
    helpers.transform_table(
        'environment', {}, {},
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.Column('id', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('tenant_id', sa.String(length=36), nullable=False),
        sa.Column('version', sa.BigInteger(), nullable=False),
        sa.Column('description', sa.Text(length=1048576), nullable=False),
        sa.Column('networking', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('tenant_id', 'name'),
        mysql_engine=MYSQL_ENGINE,
        mysql_charset=MYSQL_CHARSET
    )
    helpers.transform_table(
        'session', {}, {},
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('environment_id', sa.String(length=255), nullable=True),
        sa.Column('user_id', sa.String(length=36), nullable=False),
        sa.Column('state', sa.String(length=36), nullable=False),
        sa.Column('description', sa.Text(length=1048576), nullable=False),
        sa.Column('version', sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(['environment_id'], ['environment.id'], ),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine=MYSQL_ENGINE,
        mysql_charset=MYSQL_CHARSET
    )
    engine.execute('SET FOREIGN_KEY_CHECKS=1')

    # end Alembic commands #


def downgrade():
    engine = op.get_bind()
    engine.execute('SET FOREIGN_KEY_CHECKS=0')
    helpers.transform_table(
        'environment', {}, {},
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.Column('id', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('tenant_id', sa.String(length=36), nullable=False),
        sa.Column('version', sa.BigInteger(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('networking', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('tenant_id', 'name'),
        mysql_engine=MYSQL_ENGINE,
        mysql_charset=MYSQL_CHARSET
    )
    helpers.transform_table(
        'session', {}, {},
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('environment_id', sa.String(length=255), nullable=True),
        sa.Column('user_id', sa.String(length=36), nullable=False),
        sa.Column('state', sa.String(length=36), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('version', sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(['environment_id'], ['environment.id'], ),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine=MYSQL_ENGINE,
        mysql_charset=MYSQL_CHARSET
    )
    engine.execute('SET FOREIGN_KEY_CHECKS=1')

    # end Alembic commands #
