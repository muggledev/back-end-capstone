import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime

class MagicalPreserves(db.Model):
    __tablename__ = "MagicalPreserves"

    preserve_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    preserve_name = db.Column(db.String(150), unique=True, nullable=False)
    location = db.Column(db.String(255))
    status = db.Column(db.String(50))
    founded_date = db.Column(DateTime)

    artifacts = db.relationship(
        "Artifacts",
        secondary="PreserveArtifacts",
        back_populates="preserves"
    )
    light_creatures = db.relationship("LightCreatures", back_populates="preserve")
    dark_creatures = db.relationship("DarkCreatures", back_populates="preserve")
    caretakers = db.relationship("Caretakers", back_populates="preserve")

    def __init__(self, preserve_name, location, status, founded_date):
        self.preserve_name = preserve_name
        self.location = location
        self.status = status
        self.founded_date = founded_date
    
    def new_magical_preserves_obj():
        return MagicalPreserves('', '', '', '')

class MagicalPreservesSchema(ma.Schema):
    class Meta:
        fields = ['preserve_id', 'preserve_name', 'location', 'status', 'founded_date', 'caretakers', 'light_creatures', 'dark_creatures', 'artifacts']

    preserve_id = ma.fields.UUID()
    preserve_name = ma.fields.String()
    location = ma.fields.String()
    status = ma.fields.String()
    founded_date = ma.fields.DateTime()
    caretakers = ma.fields.Nested('CaretakersSchema', many=True, exclude=['preserve'])
    light_creatures = ma.fields.Nested('LightCreaturesSchema', many=True, exclude=['preserve'])
    dark_creatures = ma.fields.Nested('DarkCreaturesSchema', many=True, exclude=['preserve'])
    artifacts = ma.fields.Nested('ArtifactsSchema', many=True, exclude=['preserves'])

magical_preserve_schema = MagicalPreservesSchema()
magical_preserves_schema = MagicalPreservesSchema(many=True)