test = {
  'name': 'ordered?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ordered? '(1 2 3 4 5))  ; True or False
          60c2a5359961375936a02892ac434f71
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(1 5 2 4 3))  ; True or False
          30fee613b5f24feb0ea2d5089730e609
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(2 2))  ; True or False
          60c2a5359961375936a02892ac434f71
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(1 2 2 4 3))  ; True or False
          30fee613b5f24feb0ea2d5089730e609
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw07)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
