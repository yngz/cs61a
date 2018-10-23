test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 2 5)
          d1c05859088731cddc25d57af25e5e7d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 10 3)
          9f6b25a938d2c535093b558cfd80db4c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 3 3)
          79243357e7940aa5b7c895d9a8f545ce
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
