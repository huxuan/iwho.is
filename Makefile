babel-extract:
	pybabel extract -F babel.cfg -o messages.pot src/app
babel-update:
	pybabel update -i messages.pot -d src/app/translations
babel-compile:
	pybabel compile -d src/app/translations
babel-zh-init:
	pybabel init -i messages.pot -d src/app/translations -l zh
clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
run:
	./src/run.py
