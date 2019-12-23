#coding=utf-8

# 同步执行

import asyncio

# 声明异步函数
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

# 声明异步函数
async def main(urls):
    for url in urls:
        await crawl_page(url)


# time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
