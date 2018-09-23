test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> soda_reviews = [make_review('Soda', 4.5),
          ...                 make_review('Soda', 4)]
          >>> soda = make_restaurant('Soda', [127.0, 0.1],
          ...                        ['Restaurants', 'Breakfast & Brunch'],
          ...                        1, soda_reviews)
          >>> restaurant_name(soda)
          'Soda'
          >>> restaurant_location(soda)
          [127.0, 0.1]
          >>> restaurant_categories(soda)
          ['Restaurants', 'Breakfast & Brunch']
          >>> restaurant_price(soda)
          1
          >>> restaurant_ratings(soda)
          [4.5, 4]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from abstractions import *
      >>> import abstractions
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(abstractions, rest=False)
          >>> make_review = abstractions.make_review
          >>> soda_reviews = [make_review('Soda', 4.5),
          ...                 make_review('Soda', 4)]
          >>> soda = make_restaurant('Soda', [127.0, 0.1],
          ...                        ['Restaurants', 'Breakfast & Brunch'],
          ...                        1, soda_reviews)
          >>> restaurant_name(soda)
          'Soda'
          >>> restaurant_location(soda)
          [127.0, 0.1]
          >>> restaurant_categories(soda)
          ['Restaurants', 'Breakfast & Brunch']
          >>> restaurant_price(soda)
          1
          >>> restaurant_ratings(soda)
          [4.5, 4]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from abstractions import *
      >>> import abstractions
      >>> import tests.test_functions as test
      """,
      'teardown': r"""
      >>> test.restore_implementations(abstractions)
      """,
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> cory_reviews = [make_review('Cory', 2),
          ...                 make_review('Cory', 4.5),
          ...                 make_review('Cory', 1)]
          >>> cory = make_restaurant('Cory', [128.0, 0.1],
          ...                        ['Cafe', 'Boba', 'Tea'],
          ...                        2, cory_reviews)
          >>> restaurant_name(cory)
          'Cory'
          >>> restaurant_location(cory)
          [128.0, 0.1]
          >>> restaurant_categories(cory)
          ['Cafe', 'Boba', 'Tea']
          >>> restaurant_price(cory)
          2
          >>> restaurant_ratings(cory)
          [2, 4.5, 1]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from abstractions import *
      >>> import abstractions
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
