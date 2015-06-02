def url(id, status):
  return 'http://intense-crag-9901.herokuapp.com/' + str(id) + '/status?status=' + status

def setup_out(pins):
  for pin in pins:
    io.setup(pin, io.OUT)

def setup_in(pins):
  for pin in pins:
    io.setup(pin, io.IN, pull_up_down=io.PUD_UP)