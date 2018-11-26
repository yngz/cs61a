test = {
  'name': 'nodots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (nodots '(1 . 2))
          (1 2)
          scm> (nodots '(1 2 . 3))
          (1 2 3)
          scm> (nodots '((1 . 2) 3))
          ((1 2) 3)
          scm> (nodots '(1 (2 3 . 4) . 3))
          (1 (2 3 4) 3)
          scm> (nodots '(1 . ((2 3 . 4) . 3)))
          (1 (2 3 4) 3)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab13_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
