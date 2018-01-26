def app(environ, start_response):
  my_query_str = environ.get('QUERY_STRING')
  res_str = my_query_str.split('&')

  status  = '200 OK'
  headers  =  [('Content-Type', 'text/plain')]
  body = [bytes(i+'\n', 'ascii') for i in res_str  ]
  start_response(status, headers)
  return body





