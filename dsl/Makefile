.PHONY:lsp interpreter
build:
	@mkdir -p fgl/data
	@mkdir -p fgl/dsl
	@antlr4 -o fgl/dsl -listener -visitor -Dlanguage=Python3 FGL.g4
	@mv fgl/dsl/*.interp fgl/data/
	@mv fgl/dsl/*.tokens fgl/data/


test:
	@python3 -m unittest -v

coverage:
	@python3 -m coverage run -m unittest -v
	@python3 -m coverage report -m 
	@python3 -m coverage html -d data/htmlcov
	@python3 -m http.server 8001 -d data/htmlcov

dot:
	@dot -Tpng t.dot -o dot.png 

interpreter:
	@while true;do python3.10 -m interpreter.demo --ws;done

