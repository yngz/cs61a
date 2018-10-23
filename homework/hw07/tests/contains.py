test = {
  'name': 'contains?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (contains? odds 3)   ; True or False
          60c2a5359961375936a02892ac434f71
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (contains? odds 9)   ; True or False
          60c2a5359961375936a02892ac434f71
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (contains? odds 6)   ; True or False
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
      scm> (define odds (list 3 5 7 9))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
