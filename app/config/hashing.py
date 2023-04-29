from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPwd:
    def bcrypt(self: str):
        return pwd_cxt.hash(self)
