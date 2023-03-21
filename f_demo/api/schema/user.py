from conf.database import ma
from api.db.users import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ['id', 'email', "username"]
