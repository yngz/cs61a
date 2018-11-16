test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          cat|Clair de Lune|blue|forest green
          cat|Clair de Lune|blue|pink
          cat|Clair de Lune|blue|green
          cat|Clair de Lune|blue|light pink and tiffany blue
          tiger|The Middle|green|blue
          tiger|The Middle|green|periwinkle
          dog|Smells Like Teen Spirit|blue|black
          dog|Smells Like Teen Spirit|blue|gray
          dog|Smells Like Teen Spirit|blue|blue
          dog|Smells Like Teen Spirit|blue|orange
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
