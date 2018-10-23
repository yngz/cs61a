test = {
  'name': 'union',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (union odds (list 2 3 4 5))
          ab62986e44bbdd7a434838b9a55dca87
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds (list 2 4 6 8))
          58b43efdba6d06c6cd5be7ad51f88965
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds eight)
          f845c1cff169b6e1852575f7a85ba263
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
      scm> (define eight (list 1 2 3 4 5 6 7 8))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
