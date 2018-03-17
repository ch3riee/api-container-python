from express.decorators import service, methods, url


#@url('/absolute/url')
#@url('test/plain')
@service
def xyz(req, res, *args, **kwargs):
    res.json({'test': 123, 'hello': 'please'})


@service
def abc(req, res, *args, **kwargs):
	res.json({'yes': 123})

@service
def hello(req, res, *args, **kwargs):
	res.json({'hello': 'hello'})
