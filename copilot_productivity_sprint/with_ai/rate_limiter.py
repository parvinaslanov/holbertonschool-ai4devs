import time
import threading

class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate  # tokens per second
        self.tokens = float(capacity)
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def _refill(self):
        now = time.monotonic()
        elapsed = now - self.last_refill
        added_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + added_tokens)
        self.last_refill = now

    def allow_request(self, tokens_needed: int = 1) -> bool:
        with self.lock:
            self._refill()
            if self.tokens >= tokens_needed:
                self.tokens -= tokens_needed
                return True
            return False
