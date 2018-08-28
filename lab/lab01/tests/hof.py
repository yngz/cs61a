test = {
  'name': 'Higher Order Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          846abb5ea30c0c11a9a13b8ade9c2471
          # locked
          >>> chocolate
          570ba76496400e4ac020ba9d0c41fc97
          # locked
          >>> chocolate()
          357c66f38c1691dba54e404065ad7af7
          33e457ef391b3d6a9349de369aa102b7
          # locked
          >>> more_chocolate, more_cake = chocolate(), cake
          357c66f38c1691dba54e404065ad7af7
          # locked
          >>> more_chocolate
          33e457ef391b3d6a9349de369aa102b7
          # locked
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return chocolate
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          570ba76496400e4ac020ba9d0c41fc97
          # locked
          >>> snake(10, 20)()
          357c66f38c1691dba54e404065ad7af7
          33e457ef391b3d6a9349de369aa102b7
          # locked
          >>> cake = 'cake'
          >>> snake(10, 20)
          2834886dfff8faf4e4a46d07ae827d86
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
