# encoding:utf-8
import redis
import time


def set(key, value):
    client = getInstance()
    client.setnx(key, value)

def get(key):
    client = getInstance()
    return client.get(key)

def acquireLock(lock_key, LOCK_TIMEOUT):
    redis_client = getInstance()
    lock = 0
    # 获取锁
    while lock != 1:
        now = int(time.time())
        lock_timeout = now + LOCK_TIMEOUT + 1
        lock = redis_client.setnx(lock_key, lock_timeout)
        if lock == 1 or (now > int(redis_client.get(lock_key))) and now > int(redis_client.getset(lock_key, lock_timeout)):
            break
        else:
            time.sleep(0.001)
    return lock;

def releaseLock(lock_key):
    redis_client = getInstance()
    # 释放锁
    now = int(time.time())
    if now < int(redis_client.get(lock_key)):
        redis_client.delete(lock_key)



def getInstance():
    pool = redis.ConnectionPool(host='172.16.2.124', port=6379)
    # pool = redis.ConnectionPool(host='172.16.2.112', port=6379, password="redis")
    client = redis.Redis(connection_pool=pool)
    return client



if __name__ == '__main__':
    key = 'abin'
    value = 'lee'
    # set(key, value)
    result = get(key)
    print "result=",result