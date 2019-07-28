### 运行步骤
1. 运行该任务  
`celery -A tasks worker --loglevel=info`  
-A 指定创建的celery对象的位置

2. 开启Python，运行以下命令  
```python
from tasks import add
res = add.delay(4, 3)
```
