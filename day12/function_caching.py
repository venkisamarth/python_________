import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n): 
    print("caluculationg fib",n)
    if n<2: 
        return n 
    return fib(n-1) + fib(n-2)

print(fib(10))
print(time.time())
print(fib(10))
print(time.time())


from functools import lru_cache
import time 
# dummy database function 
@lru_cache(maxsize=None)
def get_user_from_db(user_id): 
    print("Fetching from database...")
    time.sleep(2)
    return {"id":user_id,"name":"user"+str(user_id)}
print(get_user_from_db(101))
print(get_user_from_db(101))













