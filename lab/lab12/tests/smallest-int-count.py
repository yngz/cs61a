test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 50;
          1|189
          2|20
          3|29
          4|11
          5|12
          6|16
          7|16
          8|13
          9|14
          11|8
          12|5
          13|1
          14|5
          15|1
          16|2
          17|3
          18|2
          19|8
          20|1
          22|3
          23|5
          24|2
          26|5
          27|3
          29|2
          31|1
          32|2
          33|1
          36|1
          37|3
          38|2
          39|2
          41|2
          42|1
          43|2
          44|1
          46|2
          47|2
          49|1
          53|1
          54|1
          55|1
          58|1
          60|1
          64|1
          69|3
          79|2
          83|1
          84|1
          96|1
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
