import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

class DarkCreatures(db.Model):
    __tablename__ = "DarkCreatures"

    dark_creature_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    preserve_id = db.Column(UUID(as_uuid=True), db.ForeignKey("MagicalPreserves.preserve_id"))
    species = db.Column(db.String(100))
    threat_level = db.Column(db.Integer)
    containment_status = db.Column(db.String(100))

    def __init__(self, preserve_id, species, threat_level, containment_status):
        self.preserve_id = preserve_id
        self.species = species
        self.threat_level = threat_level
        self.containment_status = containment_status

class DarkCreaturesSchema(ma.Schema):
    class Meta:
        fields = ['dark_creature_id', 'preserve', 'species', 'threat_level', 'containment_status']

    preserve = ma.fields.Nested('MagicalPreservesSchema')
    dark_creature_id = ma.fields.UUID()
    species = ma.fields.Str()
    threat_level = ma.fields.Int()
    containment_status = ma.fields.Str()

dark_creature_schema = DarkCreaturesSchema()
