import sys
from flask import Flask, jsonify, render_template, request
from models import db, Track
from schemas import ma, tracks_schema
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@172.17.0.1/restest'

db.init_app(app)
ma.init_app(app)


@app.route('/api/tracks/', methods=['GET'])
def list_tracks():
    if request.args.get('q'):
        q = request.args.get('q')
        tracks = Track.query.filter(Track.name.contains(q))
    else:
        tracks = Track.query.all()
    return tracks_schema.jsonify(tracks)


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    if 'createdb' in sys.argv:
        with app.app_context():
            db.create_all()
        print("Database created!")

    elif 'seeddb' in sys.argv:
        with app.app_context():
            t1 = Track(id=uuid.uuid4(), name="Never Hit Bro")
            t2 = Track(id=uuid.uuid4(), name="Oh boy")
            t3 = Track(id=uuid.uuid4(), name="Ze fox")
            db.session.add_all([t1, t2, t3])
            db.session.commit()
        print("Database seeded!")

    else:
        app.run(debug=True)
