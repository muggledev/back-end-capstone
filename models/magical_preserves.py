import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

class MagicalPreserves(db.Model):
    __tablename__ = "MagicalPreserves"

    preserve_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    preserve_name = db.Column(db.String(150), unique=True, nullable=False)
    location = db.Column(db.String(255))
    status = db.Column(db.String(50))
    founded_date = db.Column(db.Date)

    artifacts = db.relationship(
        "Artifacts",
        secondary="PreserveArtifacts",
        backref="preserves"
    )
    light_creatures = db.relationship("LightCreatures", backref="preserve")
    dark_creatures = db.relationship("DarkCreatures", backref="preserve")

    def __init__(self, preserve_name, location, status, founded_date):
        self.preserve_name = preserve_name
        self.location = location
        self.status = status
        self.founded_date = founded_date

class MagicalPreservesSchema(ma.Schema):
    class Meta:
        fields = ['preserve_id', 'preserve_name', 'location', 'status', 'founded_date', 'caretakers', 'light_creatures', 'dark_creatures', 'artifacts']

    preserve_id = ma.fields.UUID()
    preserve_name = ma.fields.Str()
    location = ma.fields.Str()
    status = ma.fields.Str()
    founded_date = ma.fields.Date()
    caretakers = ma.fields.Nested('CaretakersSchema', many=True, allow_none=True)
    light_creatures = ma.fields.Nested('LightCreaturesSchema', many=True, allow_none=True)
    dark_creatures = ma.fields.Nested('DarkCreaturesSchema', many=True, allow_none=True)
    artifacts = ma.fields.Nested('ArtifactsSchema', many=True, allow_none=True)

magical_preserve_schema = MagicalPreservesSchema()
