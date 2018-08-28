test = {
  'name': 'Truthiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 or True
          5154670fa295caf18cafa4245c1358a9
          # locked
          >>> not '' or not 0 and False
          5154670fa295caf18cafa4245c1358a9
          # locked
          >>> 13 and False
          5dfeeb9ca37d955606d40c6553cd4956
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> False or 1
          f26f9ec9ba426ebfdd8a43b22c8c74a0
          # locked
          >>> '' or 1 and 1/0
          d7b5fd49f83e4ee318af207fc969c9f4
          # locked
          >>> not 0 and 12 or 0
          d7069594fd949c78b4021fc7911322a4
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
