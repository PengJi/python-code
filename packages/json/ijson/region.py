# -*- coding: utf-8 -*-

import sys
import ijson
# import ijson.backends.yajl2_cffi as ijson

"""
https://github.com/isagalaev/ijson
http://www.aylakhan.tech/?p=27
"""

store_file = "/Users/pengji/store.txt"
region_file = "/Users/pengji/sandbox_regions.txt"

def load_json(filename):
    with open(filename, 'rb') as fd:
        parser = ijson.parse(fd)
        for prefix, event, value in parser:
            print('prefix={}, event={}, value={}'.format(prefix, event, value))

def get_ins(file_name):
    """
    得到位于同一机器的实例
    Args:
        file_name:

    Returns:
        列表
    """
    addr_store = {}
    with open(file_name, 'r') as fp:
        objects = ijson.items(fp, 'stores.item')
        for ob in objects:
            # print ob['store']['address'].split(':')[0], ob['store']['id']

            if not addr_store.get(ob['store']['address'].split(':')[0], 0):
                addr_store[ob['store']['address'].split(':')[0]] = [ob['store']['id']]
            else:
                addr_store[ob['store']['address'].split(':')[0]].append(ob['store']['id'])

        store = []
        for k, v in addr_store.items():
            store.append(tuple(v))

        print store

        return store

def get_region(file_name, ins=None):
    """
    判断region
    Args:
        file_name:
        ins: 实例

    Returns:

    """
    region_store = {}
    with open(file_name, 'r') as fp:
        peers = ijson.items(fp, 'regions.item.peers.item')
        for ob in peers:
            region_store[ob['id']] = ob['store_id']

        sys.getsizeof(region_store)

    with open(file_name, 'r') as fp:
        regions = ijson.items(fp, 'regions.item')
        tmp = []
        for ob in regions:
            tmp.append(region_store[ob['id']])
            for k in ob['peers']:
                tmp.append(k['store_id'])

            for s in ins:
                res = [store for store in s if store in tmp]
                if len(res):
                    print res


if __name__ == '__main__':
    # load_json(store_file)
    ins = get_ins(store_file)
    get_region(region_file, ins)