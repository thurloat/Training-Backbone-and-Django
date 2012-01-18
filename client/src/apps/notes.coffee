class NotesApplication
  run: ->
    # create instances of view classes
    # do any additional booting (bootstrapping data?)
    # push go
    alert "Hello Developers"
    
    
# jQuery document.onready
$ ->
  if not jasmine?
    @app = new NotesApplication
    do @app.run
    