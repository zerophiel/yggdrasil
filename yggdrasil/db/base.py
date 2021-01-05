# Import all the models, so that Base has them before being
# imported by Alembic
from yggdrasil.db.base_class import Base  # noqa
from yggdrasil.models.domain.item import Item  # noqa
from yggdrasil.models.domain.user import User  # noqa
