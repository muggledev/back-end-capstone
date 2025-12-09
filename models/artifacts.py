import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

class Artifacts(db.Model):
    __tablename__ = "Artifacts"

    artifact_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    artifact_name = db.Column(db.String(150), unique=True, nullable=False)
    artifact_type = db.Column(db.String(100))
    power_level = db.Column(db.Integer)
    is_cursed = db.Column(db.Boolean, default=False)

    def __init__(self, artifact_name, artifact_type, power_level, is_cursed=False):
        self.artifact_name = artifact_name
        self.artifact_type = artifact_type
        self.power_level = power_level
        self.is_cursed = is_cursed

class ArtifactsSchema(ma.Schema):
    class Meta:
        fields = ['artifact_id', 'artifact_name', 'artifact_type', 'power_level', 'is_cursed', 'preserves']

    artifact_id = ma.fields.UUID()
    artifact_name = ma.fields.Str()
    artifact_type = ma.fields.Str()
    power_level = ma.fields.Int()
    is_cursed = ma.fields.Bool()
    preserves = ma.fields.Nested('MagicalPreservesSchema', many=True, allow_none=True)

artifact_schema = ArtifactsSchema()
