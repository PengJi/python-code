### 运行步骤
1. 启动worker  
`celery -A proj worker -l info`

2. 进入proj的上一级目录
```python
from proj.tasks import add
add.delay(2, 2)
add.apply_async((2, 2))
add.apply_async((2, 2), queue='lopri', countdown=10)
add(2, 2)

# 得到结果
res = add.delay(2, 2)
res.get(timeout=1)
print res.id

# 获取异常
res = add.delay(2)
res.get(timeout=1)

# 判断状态
res.failed()
res.successful()

```