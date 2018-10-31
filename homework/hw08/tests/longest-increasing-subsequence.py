test = {
  'name': 'longest-increasing-subsequence',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (longest-increasing-subsequence '())
          ()
          scm> (longest-increasing-subsequence '(1))
          (1)
          scm> (longest-increasing-subsequence '(1 2 3))
          (1 2 3)
          scm> (longest-increasing-subsequence '(1 9 2 3))
          (1 2 3)
          scm> (longest-increasing-subsequence '(1 9 8 7 6 5 4 3 2 3))
          (1 2 3)
          scm> (longest-increasing-subsequence '(1 9 8 7 2 3 6 5 4 5))
          (1 2 3 4 5)
          scm> (longest-increasing-subsequence '(1 2 3 4 9 3 4 1 10 5))
          (1 2 3 4 9 10)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
