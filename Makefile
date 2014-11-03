babel-extract:
	pybabel extract -F babel.cfg -o messages.pot src/app
babel-update:
	pybabel update -i messages.pot -d src/app/translations
babel-compile:
	pybabel compile -d src/app/translations
babel-zh-init:
	pybabel init -i messages.pot -d src/app/translations -l zh
