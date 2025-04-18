from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)  # Hash before storing
    
    @staticmethod
    def verify(hashed_password: str, plain_password: str):
        return pwd_context.verify(plain_password, hashed_password)  # Verify correctly
