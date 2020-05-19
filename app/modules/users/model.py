from app import db

## DEFINE MODELS

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, unique=True, nullable=True)
  email = db.Column(db.String, unique=True, nullable=True)
  password = db.Column(db.String(255))
  active = db.Column(db.Boolean())
  roles = db.relationship('Role', secondary=roles_users,
                          backref=db.backref('users', lazy='dynamic'))

  # METHODS
  @property
  def rolenames(self):
      try:
          roles = self.roles.all()
          return [roles.name for role in roles]
      except Exception:
          return []

  @classmethod
  def lookup(cls, username):
      return cls.query.filter_by(username=username).one_or_none()

  @classmethod
  def identify(cls, id):
      return cls.query.get(id)

  @property
  def identity(self):
      return self.id

  def is_valid(self):
      return self.active
