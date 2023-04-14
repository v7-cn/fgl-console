.PHONY:fgl lsp interpreter engine
# fgl command init
alias:
	@echo 'alias fgl="python3 -m interpreter.cli"'
# 语法编译
build: 
	@mkdir -p fgl/data
	@mkdir -p fgl/dsl
	@antlr4 -o fgl/dsl -listener -visitor -Dlanguage=Python3 fgl/FGL.g4
	@mv fgl/dsl/*.interp fgl/data/
	@mv fgl/dsl/*.tokens fgl/data/

# 语法测试
test:
	@python3 -m unittest -v

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

# engine cli submit
cli-submit:
	python3 -m interpreter.cli exec -c "CALL PARADIGM attribute_transductive('Cora', 500)" -r

# engine cli paradigm command
cli-paradigm:
	python3 -m interpreter.cli attribute-transduction --epoch 300

# engine cli paradigm command
cli-paradigm-submit:
	python3 -m interpreter.cli attribute-transduction --epoch 300 -r

# engine server daemon
daemon:
	dagster dev  -m engine.engine --dagit-host=0.0.0.0




