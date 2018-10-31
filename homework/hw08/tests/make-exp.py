test = {
  'name': 'make-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-exp 2 4)
          43fb0199e9e2345f8b8a767d78463c89
          # locked
          scm> (make-exp 'x 1)
          36e066bfc6378b709f8c41ed98771eb2
          # locked
          scm> (make-exp 'x 0)
          38dac9033a8f5e8edb2dbe6428e02d1d
          # locked
          scm> x^2
          37c446142756e6233e39a8a175b02f82
          # locked
          scm> (base x^2)
          36e066bfc6378b709f8c41ed98771eb2
          # locked
          scm> (exponent x^2)
          bec7b0c91bdcb548cda9e9f3546cf0d7
          # locked
          scm> (exp? x^2) ; True or False
          af2fd7905919be94e4d509e8239d5fd1
          # locked
          scm> (exp? 1)
          3cbee9249bf6c5fe6fce86debf3b010a
          # locked
          scm> (exp? 'x)
          3cbee9249bf6c5fe6fce86debf3b010a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
