from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
from pygments.lexers.sql import SqlLexer

SQLCompleter = WordCompleter(['SLECET', 'SHOW', 'FROM', 'WHERE'], ignore_case=True)

while 1:
	inp = prompt(u'>> ',
				 history=FileHistory('history.txt'),
				 auto_suggest=AutoSuggestFromHistory(),
				 completer=SQLCompleter,
				 lexer=SqlLexer  # syntax highlighting
				 )
	if inp == "quit":
		break
	print(inp)
