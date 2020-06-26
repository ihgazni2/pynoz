>>> xt = datetime.datetime.strptime('Sat Jun 20 2020 08:00:00 GMT+0800',"%a %b %d %Y %H:%M:%S %Z%z")
>>> yt = datetime.datetime.strptime('Sat Jun 20 2020 08:00:00',"%a %b %d %Y %H:%M:%S")
>>>
>>> xt.timestamp()
1592611200.0
>>> yt.timestamp()
1592640000.0
>>> zt = datetime.datetime.strptime('Sat Jun 20 2020 00:00:00',"%a %b %d %Y %H:%M:%S")
>>> zt.timestamp()
1592611200.0
>>>

