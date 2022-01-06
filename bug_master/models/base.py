from sqlalchemy.orm import Session

from bug_master.database import Base

from ..consts import logger


class BaseModule(Base):
    __abstract__ = True

    @classmethod
    def create(cls, session: Session, **kwargs) -> Base:
        """Create or get if already exist"""

        _id = kwargs.get("id", "")
        instance = session.query(cls).filter_by(id=_id).first()

        if not instance:
            instance = cls(**kwargs)
            session.add(instance)
            session.commit()
            logger.info(f"Added new entry to {cls.__tablename__} table, with id {_id}")

        return instance