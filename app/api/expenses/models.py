from app import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable = False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date,nullable=False)
    description = db.Column(db.String(255))


