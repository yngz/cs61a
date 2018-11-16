test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from fa18favpets;
          dog|58
          cat|22
          tiger|10
          dolphin|9
          elephant|9
          panda|9
          dragon|7
          koala|7
          lion|7
          corgi|6
          sqlite> SELECT * from fa18dog;
          dog|58
          sqlite> SELECT * from fa18alldogs;
          dog|75
          sqlite> SELECT * from obedienceimages;
          7|Image 1|20
          7|Image 2|22
          7|Image 3|36
          7|Image 4|44
          7|Image 5|16
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
