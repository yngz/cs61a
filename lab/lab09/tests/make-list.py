test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a '(1))
          d1600efb42ba062004d543878f62c850
          # locked
          scm> a
          de14f22fe5379b349d7d23f00aa8b3d3
          # locked
          scm> (define b (cons 2 a))
          374bf313072010f8272e1b91c3d7e080
          # locked
          scm> b
          3e447cd57f0ec893409ff671c7d6648f
          # locked
          scm> (define c (list 3 b))
          f01e532ff092129162f319054ab0cb3c
          # locked
          scm> c
          f320afce4c31d735664db15215dd5628
          # locked
          scm> (car c)
          aa358e49beb94f999014e1c16f14faf8
          # locked
          scm> (cdr c)
          104798f1c7a26e19a2d11dd8dc55c6cd
          # locked
          scm> (car (car (cdr c)))
          242a6d3d4ed1b1d1292acd307083f4e0
          # locked
          scm> (cdr (car (cdr c)))
          de14f22fe5379b349d7d23f00aa8b3d3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> lst  ; type out exactly how Scheme would print the list
          1b56df4e12214e2eff032931fb8c18e9
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
