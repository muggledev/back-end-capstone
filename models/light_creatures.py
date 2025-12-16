import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

class LightCreatures(db.Model):
    __tablename__ = "LightCreatures"

    light_creature_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    preserve_id = db.Column(UUID(as_uuid=True), db.ForeignKey("MagicalPreserves.preserve_id"))
    species = db.Column(db.String(100))
    personality = db.Column(db.String(255))
    magic_ability = db.Column(db.String(255))
    danger_level = db.Column(db.Integer)

    preserve = db.relationship("MagicalPreserves", back_populates="light_creatures")

    def __init__(self, preserve_id, species, personality, magic_ability, danger_level):
        self.preserve_id = preserve_id
        self.species = species
        self.personality = personality
        self.magic_ability = magic_ability
        self.danger_level = danger_level

    def new_light_creatures_obj():
        return LightCreatures('', '', '', '', 0)

class LightCreaturesSchema(ma.Schema):
    class Meta:
        fields = ['light_creature_id', 'preserve', 'species', 'personality', 'magic_ability', 'danger_level']

    preserve = ma.fields.Nested('MagicalPreservesSchema', exclude=['light_creatures'])
    light_creature_id = ma.fields.UUID()
    species = ma.fields.String()
    personality = ma.fields.String()
    magic_ability = ma.fields.String()
    danger_level = ma.fields.Integer()

light_creature_schema = LightCreaturesSchema()
light_creatures_schema = LightCreaturesSchema(many=True)