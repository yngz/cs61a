test = {
  'name': 'Mutability',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> lst = [5, 6, 7, 8]
          >>> lst.append(6)
          Nothing
          >>> lst
          [5, 6, 7, 8, 6]
          >>> lst.insert(0, 9)
          >>> lst
          [9, 5, 6, 7, 8, 6]
          >>> x = lst.pop(2)
          >>> lst
          [9, 5, 7, 8, 6]
          >>> lst.remove(x)
          >>> lst
          [9, 5, 7, 8]
          >>> a, b = lst, lst[:]
          >>> a is lst
          True
          >>> b == lst
          True
          >>> b is lst
          False
          """
        },
      ]
    },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          25
          >>> len(pokemon)
          3
          >>> pokemon['jolteon'] = 135
          >>> pokemon['mew'] = 25
          >>> len(pokemon)
          4
          >>> 'mewtwo' in pokemon
          False
          >>> 'pikachu' in pokemon
          True
          >>> 25 in pokemon
          False
          >>> 148 in pokemon.values()
          True
          >>> 151 in pokemon.keys()
          False
          >>> 'mew' in pokemon.keys()
          True
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> pokemon['ditto']
          135
          """
        },
      ]
    }
  ]
}
