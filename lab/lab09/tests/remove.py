test = {
  'name': 'remove',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (remove 3 nil)
          f9ebafa0bfa75e2a858c464aa39a573d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 2 '(1 3 2))
          4274c7da2de8112f582f10ef20b2d371
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 1 '(1 3 2))
          a69c1998a934bceac4c7b234f084e250
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 42 '(1 3 2))
          09c9e5e54b16e44b6676cd663e135ab4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 3 '(1 3 3 7))
          14857fc721cca1cd17cf1d9e3404fd2a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
