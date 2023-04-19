# slht-fgl-lite
# FGL
Formalized Graph AI Language（缩写：**FGL**）是由Graph AI标准化范式驱动的声明式业务智能应用开发语言

**FGL项目的目标**：一行代码实现业务化图神经网络模型搭建。
> CV与NLP飞速发展大大加速了AGI，然而在**海量业务决策**问题中真正需要的是思考**事物和事物之间的关系**，这就意味着必须利用Graph AI相关技术才能有效帮助AI厘清事物间关系做出有效决策。    
> Graph作为一种灵活的数据结构，优势是可以表达所有事物间关系，但同时也意味着模型的构建与拟合变得更加复杂。**如何将Graph AI模型构建变得更加简单**，变得不再需要深入了解底层图神经网络算法，变得像使用数据库一样成为一种程序员的基本技能，是我们不断希望达到的目标。  
> 为此，我们提出了**范式化抽象**，即Graph AI标准化范式，将Graph AI所能够解决的每一类问题抽象成一类范式。只要业务问题匹配范式，并提供相应的输入，FGL会自动构建最优的Graph AI模型对数据进行拟合。不再需要思考算法、思考Loss Function、思考参数等等细节问题。  

# 目录说明 
* fgl FGL语法支持
* interpreter FGL语法解释器
* interpreter/engine_adapters 针对不同计算引擎的适配器
* engine 计算引擎
* libs 算子库
* examples 样例
* requirements.txt 依赖项

# 安装
## 容器运行环境[建议]
    > docker build -t fglite ./docker
## 本地运行环境[不推荐]
    > python setup.py install 

# 使用
## 特性
* 执行命令  
docker run -v $PWD:/data -it fglite ```fgl -c "{FGL}"```

* 执行fgl脚本  
docker run -v $PWD:/data -it fglite ```fgl -s examples/paradigm.fgl```

* automl支持

* 报告支持

## 范式
* 执行命令  
    > docker run -v $PWD:/data -it fglite ```fgl -c "{FGL}"```
* 属性传导范式
    * 训练 
    > ```TRAIN PARADIGM attribute_transduction WHERE name='Cora' AND automl=true AND trials=10 AND output='model'```
    * 预测  
    > ```PREDICT PARADIGM attribute_transduction WHERE name='Cora' AND model='model' AND output='classes.txt'```

* 向量化匹配范式
    * 训练 
    > ```TRAIN PARADIGM vector_matching WHERE name='./data/cora.json' AND automl=true AND trials=10 AND output='model'```
    * 预测  
    > ```PREDICT PARADIGM vector_matching WHERE name='./data/cora.json' AND model='model' AND output='embedding.txt'```

* 时序图范式
    * 训练 
    > ```TRAIN PARADIGM temporal_evolution WHERE name='chickenpox' AND automl=true AND trials=10 AND output='model'```
    * 预测  
    > ```PREDICT PARADIGM temporal_evolution WHERE name='./data/chickenpox.json' AND model='model' AND output='temporal.txt'```

# 贡献
描述如何参与项目开发，包括：
- 如何构建项目
 > make build-grammar   
 > make build 

- 如何运行测试
> make test-grammar   
> make test   

- 贡献指南

- 开发规范

# 版权和许可证
列出该项目的版权和许可证信息。

# 作者
列出该项目的作者和联系方式。可以包含以下内容：
- 作者姓名
- 邮箱地址
- 博客地址
- 社交媒体账号

# 致谢
向为该项目做出贡献的人员致谢。可以列出他们的姓名和贡献方式。