from flask_marshmallow import Marshmallow
from models import Track

ma = Marshmallow()


class TrackSchema(ma.ModelSchema):
    class Meta:
        model = Track

track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)