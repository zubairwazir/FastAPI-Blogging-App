from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    def bcrypt(self: str):
        return pwd_cxt.hash(self)

    def verify(plain_passowrd, hashed_password):
        return pwd_cxt.verify(plain_passowrd, hashed_password)
