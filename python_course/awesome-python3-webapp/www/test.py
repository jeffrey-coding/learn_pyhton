import orm
import asyncio
import threading
from models import User, Blog, Comment



async def test(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='jeffrey',password='0704', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
