import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

class Caretakers(db.Model):
    __tablename__ = "Caretakers"

    caretaker_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), unique=True)
    preserve_id = db.Column(UUID(as_uuid=True), db.ForeignKey("MagicalPreserves.preserve_id"))
    caretaker_name = db.Column(db.String(100), nullable=False)
    joined_date = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

    preserve = db.relationship("MagicalPreserves", backref="caretakers")

    def __init__(self, user_id, preserve_id, caretaker_name, joined_date, is_active=True):
        self.user_id = user_id
        self.preserve_id = preserve_id
        self.caretaker_name = caretaker_name
        self.joined_date = joined_date
        self.is_active = is_active

class CaretakersSchema(ma.Schema):
    class Meta:
        fields = ['caretaker_id', 'user', 'preserve', 'caretaker_name', 'joined_date', 'is_active']

    user = ma.fields.Nested('UsersSchema', allow_none=True)
    preserve = ma.fields.Nested('MagicalPreservesSchema', allow_none=True)
    caretaker_id = ma.fields.UUID()
    caretaker_name = ma.fields.Str()
    joined_date = ma.fields.DateTime()
    is_active = ma.fields.Bool()

caretaker_schema = CaretakersSchema()
