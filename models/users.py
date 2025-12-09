import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")
    is_active = db.Column(db.Boolean, default=True)

    caretaker = db.relationship("Caretakers", uselist=False, backref="user")
    tokens = db.relationship("AuthTokens", backref="user")

    def __init__(self, username, email, password_hash, role="user", is_active=True):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.is_active = is_active

class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'username', 'email', 'role', 'is_active', 'caretaker', 'tokens']

    user_id = ma.fields.UUID()
    username = ma.fields.Str()
    email = ma.fields.Str()
    role = ma.fields.Str()
    is_active = ma.fields.Bool()
    caretaker = ma.fields.Nested('CaretakersSchema', allow_none=True)
    tokens = ma.fields.Nested('AuthTokenSchema', many=True, allow_none=True)

user_schema = UsersSchema()
