class Licensing:
    def verify(self, key: str) -> bool:
        if not key:
            return False
        return key.startswith("PRO-") or key.startswith("ENT-")
