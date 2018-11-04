test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> read_line("(a . b)")
          0b0cc1b8cf08e385941c8c36b5c52b62
          # locked
          # choice: Pair('a', Pair('b'))
          # choice: Pair('a', Pair('b', nil))
          # choice: SyntaxError
          # choice: Pair('a', 'b')
          # choice: Pair('a', 'b', nil)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a b . c)")
          e0650e8b7a6620bc7853084430e25494
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: Pair('a', Pair('b', Pair('c')))
          # choice: Pair('a', 'b', 'c')
          # choice: Pair('a', Pair('b', 'c'))
          # choice: SyntaxError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a b . c d)")
          8c2bf83bd06967ba8dd8731d41d13081
          # locked
          # choice: Pair('a', Pair('b', Pair('c', 'd')))
          # choice: Pair('a', Pair('b', 'c'))
          # choice: Pair('a', Pair('b', Pair('c', Pair('d', nil))))
          # choice: SyntaxError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a . (b . (c . ())))")
          d106bb7be6b014a9d16d74410be4a8a5
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: SyntaxError
          # choice: Pair('a', Pair('b', Pair('c', Pair(nil, nil))))
          # choice: Pair('a', 'b', 'c')
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a . ((b . (c))))")
          963c3554f1b17d86bc590ef60f144da2
          # locked
          # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil))
          # choice: Pair('a', Pair('b', Pair('c', nil)), nil)
          # choice: Pair('a', Pair('b', Pair('c')), nil)
          # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil), nil)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(1 . 2)"]))
          >>> scheme_read(src)
          Pair(1, 2)
          >>> src.current() # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line('(1 2 . 3)')
          Pair(1, Pair(2, 3))
          >>> read_line('(1 . 2 3)')
          SyntaxError
          >>> scheme_read(Buffer(tokenize_lines(['(1', '2 .', "(quote (3 4)))", '4'])))
          Pair(1, Pair(2, Pair('quote', Pair(Pair(3, Pair(4, nil)), nil))))
          >>> read_line("(2 . 3 4 . 5)")
          SyntaxError
          >>> read_line("(2 (3 . 4) 5)")
          Pair(2, Pair(Pair(3, 4), Pair(5, nil)))
          >>> read_line("(1 2")
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines(['. 1)'])))
          1
          >>> read_tail(Buffer(tokenize_lines(['. 1'])))
          SyntaxError
          >>> read_tail(Buffer(tokenize_lines(['. (1 2 3))'])))
          Pair(1, Pair(2, Pair(3, nil)))
          >>> read_line("(1 . (quote (2 . (quote (3 4)))))")
          Pair(1, Pair('quote', Pair(Pair(2, Pair('quote', Pair(Pair(3, Pair(4, nil)), nil))), nil)))
          >>> read_line("(1 . (quote (2 (3 4))) 6)")
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
