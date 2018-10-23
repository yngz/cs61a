test = {
  'name': 'add',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add odds 2)
          c1f43b222f5f6e308e17941a6b97898f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 5)
          244a1e3f51a6f4afe83944c26fbf7311
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 6)
          1b7995e61fcb2eaebbda782ef7cec54d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 10)
          69d3c71b4d4f9b941dd1a197ddf3660c
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
