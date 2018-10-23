test = {
  'name': 'intersect',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (intersect odds (list 2 3 4 5))
          909d56987c11b3becce761b5871bdf47
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds (list 2 4 6 8))  ; Empty list is ()
          7b043779e02c43bdcd630251dbb3ebc9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds eight)
          3bcf331630538e53425e07db90a89840
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
