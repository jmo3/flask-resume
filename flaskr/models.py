from flaskr import db

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media = db.Column(db.String(255))
    credit = db.Column(db.String(255))
    caption = db.Column(db.Text)

    def __init__(self, media, credit, caption):
        self.media = media
        self.credit = credit
        self.caption = caption

    def __repr__(self):
        return "<Asset(media='%s', credit='%s', caption='%s')>'" % (self.media, self.credit, self.caption)

class Timeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(80))
    text = db.Column(db.Text)
    # text = db.Column(db.String(255), unique=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    asset = db.relationship('Asset',
                            backref=db.backref('timelines', lazy='dynamic'))

    def __init__(self, headline, text, asset):
        self.headline = headline
        self.text = text
        self.asset = asset

    def __repr__(self):
        return "<Timeline(headline='%s', text='%s')>'" % (self.headline, self.text)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(80))
    startDate = db.Column(db.String(80))
    endDate = db.Column(db.String(80))
    text = db.Column(db.Text)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    asset = db.relationship('Asset',
                            backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, headline, startDate, endDate, text, asset):
        self.headline = headline
        self.startDate = startDate
        self.endDate = endDate
        self.text = text
        self.asset = asset

    def __repr__(self):
        return "<Headline(headline='%s', startDate='%s', endDate='%s', text='%s')>" % (self.headline, self.startDate, self.endDate, self.text)