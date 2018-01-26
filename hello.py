def app(environ, start_response):
  my_query_str = environ.get('QUERY_STRING')
  res_str = my_query_str.replace('&','\n')

  status  = '200 OK'
  headers  =  [('Content-Type', 'text/plain')]
#  body = 'Hello,world!'
  start_response(status, headers)
  return res_str





