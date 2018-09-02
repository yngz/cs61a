test = {
  'name': 'Question 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> bacon_strategy(0, 0, margin=8, num_rolls=5)
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> bacon_strategy(70, 64, margin=6, num_rolls=5)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> bacon_strategy(50, 55, margin=5, num_rolls=5)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> bacon_strategy(32, 47, margin=5, num_rolls=4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 14, margin=1, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(bacon_strategy)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> bacon_strategy(20, 41, margin=3, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 20, margin=5, num_rolls=0)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 24, margin=7, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 25, margin=2, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 77, margin=10, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
