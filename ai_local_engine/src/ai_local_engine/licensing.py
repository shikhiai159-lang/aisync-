import hmac
import hashlib

class Licensing:
    def __init__(self, secret: str = "ai_local_engine_secret"):
        self.secret = secret.encode("utf-8")

    def verify(self, key: str) -> bool:
        if not key or not isinstance(key, str):
            return False
        
        # ফরম্যাট চেক: PRO- দিয়ে শুরু হতে হবে
        if key.startswith("PRO-") or key.startswith("ENT-"):
            return len(key) >= 12
            
        return False
