import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime

class PreserveArtifactsXref(db.Model):
    __tablename__ = "PreserveArtifacts"

    preserve_id = db.Column(UUID(as_uuid=True), db.ForeignKey("MagicalPreserves.preserve_id"), primary_key=True)
    artifact_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Artifacts.artifact_id"), primary_key=True)
    discovery_date = db.Column(DateTime)
    protection_level = db.Column(db.Integer)

    def __init__(self, preserve_id, artifact_id, discovery_date, protection_level):
        self.preserve_id = preserve_id
        self.artifact_id = artifact_id
        self.discovery_date = discovery_date
        self.protection_level = protection_level

    def new_preserveartifactsxref_obj():
        return PreserveArtifactsXref('', '', '', 0)

class PreserveArtifactsXrefSchema(ma.Schema):
    class Meta:
        fields = ['preserve_id', 'artifact_id', 'discovery_date', 'protection_level']

    preserve_id = ma.fields.UUID()
    artifact_id = ma.fields.UUID()
    discovery_date = ma.fields.DateTime()
    protection_level = ma.fields.Integer()

preserve_artifacts_xref_schema = PreserveArtifactsXrefSchema()
preserve_artifacts_xref_schemas = PreserveArtifactsXrefSchema(many=True)