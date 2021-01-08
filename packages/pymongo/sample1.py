from pymongo import *


def main():
    # 创建连接对象
    client = MongoClient(host='localhost', port=27017)

    # 获得数据库，此处使用python数据库
    db = client.python

    # 增加
    db.stu.insert_one({'name': 'name1', 'gender': '男'})
    db.stu.insert_one({'name': 'name2', 'gender': '女'})
    db.stu.insert_one({'name': 'name3', 'gender': '男'})
    db.stu.insert_one({'name': 'name4', 'gender': '男'})
    db.stu.insert_one({'name': 'name5', 'gender': '女'})

    # 查询
    # 查询一条文档
    result = db.stu.find_one({'name': 'name1'})
    print(result)

    # 查询多条文档
    result = db.stu.find({'gender': '男'})

    for item in result:
        print('%s--%s' % (item['name'], item['gender']))

    # 修改
    # 更新满足条件的第一条文档
    db.stu.update_one({'name': 'name2'}, {'$set': {'name': 'name2name2'}})

    # 更新满足条件的所有文档
    db.stu.update_many({'gender': "男"}, {'$set': {'gender': 'boy'}})

    # 删除
    # 删除满足条件的第一条文档
    db.stu.delete_one({'gender': '男'})

    # 删除满足条件的所有文档
    db.stu.delete_many({'gender': '女'})


if __name__ == '__main__':
    main()