from edison import db
import json


class Policy(db.Model):
    _tablename_ = 'policy'
    _table_args_ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    policy_name = db.Column(db.String(50), nullable=False)
    room = db.Column(db.String(50), nullable=False)
    conditions = db.Column(db.String(300), nullable=False)
    commands = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_json(self):
        return json.dump(self, defualt=lambda obj: obj.__dict__, sort_keys=True, indent=4)

    def _repr_(self):
        return f"<Policy: id = {self.id}, title = {self.title}, " \
               f"sensors= {self.sensors}, username = {self.activationTime}, email = {self.status}>"
