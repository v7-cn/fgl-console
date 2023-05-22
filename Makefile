.PHONY:fgl lsp interpreter engine 

source:
	@echo source /data3t/ty010/bin/activate
    
# fgl command init
alias:
	@echo 'alias fgl="python3 -m interpreter.cli"'
	@echo 'echo 81920 > /proc/sys/fs/inotify/max_user_watches'

# 镜像编译
build: 
	docker build -t fglite ./docker

# 语法编译
build-grammar: 
	@mkdir -p fgl/data
	@mkdir -p fgl/dsl
	@antlr4 -o fgl/dsl -listener -visitor -Dlanguage=Python3 fgl/FGL.g4
	@mv fgl/dsl/fgl/*.interp fgl/data/
	@mv fgl/dsl/fgl/*.tokens fgl/data/
	@mv fgl/dsl/fgl/*.py fgl/dsl/
	@rm -rf fgl/dsl/fgl

# 语法测试
test-grammar:
	@python3 -m unittest -v

test:
	@echo "属性传导范式[训练]"
	docker run -v ${PWD}:/data -it fglite \
		fgl -c "TRAIN PARADIGM attribute_transduction WHERE name='Cora' AND automl=true AND trials=10 AND output='model'"
	@echo "属性传导范式[预测]"
	docker run -v ${PWD}:/data -it fglite \
		fgl -c "PREDICT PARADIGM attribute_transduction WHERE name='Cora' AND  model='model' AND output='classes.txt'"
	@echo "向量化匹配范式[训练]"
	docker run -v ${PWD}:/data -it fglite \
		fgl -c "TRAIN PARADIGM vector_matching WHERE name='./data/cora.json' AND automl=true AND trials=10 AND output='model'"
	@echo "向量化匹配范式[预测]"
	docker run -v ${PWD}:/data -it fglite \
		fgl -c "PREDICT PARADIGM vector_matching WHERE name='./data/cora.json' AND  model='model' AND output='embedding.txt'"
	@echo "时序图演进范式[训练]"
	docker run -v ${PWD}:/data -it fglite \
		fgl -c "TRAIN PARADIGM temporal_evolution WHERE name='chickenpox' AND automl=true AND trials=10 AND output='model'"
	@echo "时序图演进范式[预测]"
	docker run -v ${PWD}:/data -it fglite \
		fgl -c "PREDICT PARADIGM temporal_evolution WHERE name='./data/chickenpox.json' AND  model='model' AND output='temporal.txt'"

# 语法覆盖测试
coverage:
	@python3 -m coverage run -m unittest -v
	@python3 -m coverage report -m 
	@python3 -m coverage html -d data/htmlcov
	@python3 -m http.server 8001 -d data/htmlcov

# 语法测试dot文件输出
dot:
	@dot -Tpng t.dot -o dot.png 

# 解释器测试
interpreter:
	@while true;do python3.10 -m interpreter.demo --ws;done



# engine cli run
cli-run:
	python3 -m interpreter.cli exec -c "CALL PARADIGM attribute_transductive('Cora', 500)"


# engine cli paradigm command
cli-paradigm:
	python3 -m interpreter.cli attribute-transduction --epoch 300


# engine cli submit
cli-submit:
	python3 -m interpreter.cli exec -c "CALL PARADIGM attribute_transductive('Cora', 500)" -r
	


# engine cli paradigm command
cli-paradigm-submit:
	python3 -m interpreter.cli attribute-transduction --epoch 300 -r

# engine server daemon
daemon:
	export DAGSTER_HOME=${PWD}/data && dagster dev  -m engine.engine --dagit-host=0.0.0.0




