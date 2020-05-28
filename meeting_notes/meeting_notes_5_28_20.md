Ideas on how to store results in DB. POSTPONED until 5/29

{'columns': ["x", "y"], 'ml_process': {'similarity': [[columnx,columny],[columny, columnz]]}}

'result_y_from_table': {'male': 500}

'result_y_from_table': {'male': 500, 'female': 200}

{
  'columns': ["x", "y"],
  'ml_proc_cache': {},
  'ml_proc_custom_data': 'result_y_from_table': {'Column': 500}, {'section within column': 200}
}

graph 123, it will query `ml_proc_custom_data` for `k1`

{ NO WAY OF UNDERSTANDING EVERY SINGLE EXTRA KEY + HOW TO CREATE GRAPHS
  'graphs': [[columnx,columnz, 'similarity'], [columnz,columnx, 'correlation']],
  'poi': ['columnf', 500, 'string of purpose?'],
  'outlier': ['columnf', 'coumnz'],
  'majority': ['columnf']
}

{'graph_id':[[poi: columnf, 500], 'stringofpurpose']}

{ KEPT AS 1 KEY. DATABASE DOESN'T SCALE WELL
1: {'poi': [columnf, 500, purpose]},
2: {'outlier': [blablabla]}
}

{'data_based': {'similarity': [[columnx,columny,columnz]], 'correlation': [[]]}, 'custom_metrics': {}}


{
	GRAPH_ID: XYZ,
	'POI': [columnf, 500, purpose]
}

{
	GRAPH_ID: XYZ,
	'outlier': ['columnf', 'coumnz']
}


