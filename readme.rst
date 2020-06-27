.. contents:: Table of Contents
   :depth: 5


*pynoz*
------------
- time,date,timezone,tools


Installation
============

    ::
    
        $ pip3 install pynoz

Usage
=====
    
    ::
        
        from pynoz import func
        from xdict.jprint import pobj
        
        s = "2020-06-27 08:00:00 GMT +0800"
        d = func.str2dict(s)
        >>>pobj(d)
        {
         'y': 2020,                     # year    
         'm': 6,                        # month  
         'd': 27,                       # day
         'h': 8,                        # hour
         'min': 0,                      # minute
         's': 0,                        # second
         'ms': 0,                       # millisecond
         'ts': 1593216000.0,            # timestamp-second         python
         'mts': 1593216000000.0,        # timestamp-millisecond    javascript
         'z': '+0800',                  # utc-offset-string        ±HHMM[SS[.ffffff]]
         'zone': 'Etc/GMT-8',           # zone
         'tzname': 'GMT',               # tzname    
         'soffset': 28800.0,            # seconds-offset         28800 //3600 = 8    +0800   08:00:00 
         'msoffset': 28800000.0,        # msoffset
         'yq': 2,                       # quarter-of-year
         'yw': 26,                      # week-of-year
         'yd': 177,                     # day-of-year
         'qm': 3,                       # month-of-quarter
         'qw': 13,                      # week-of-quarter
         'qd': 87,                      # day-of-quarter
         'mt': 3,                       # ten ,旬, each-ten-days, used-in-chinese
         'mw': 4,                       # week-of-month
         'td': 7,                       # day-of-ten
         'wd': 6                        # isoweekday,
        }
        >>>

        >>> dt = func.str2dt(s)
        >>> dt
        datetime.datetime(2020, 6, 27, 8, 0, tzinfo=datetime.timezone(datetime.timedelta(0, 28800), 'GMT'))
        >>>

        >>>ts = d['ts']
        >>> ts
        1593216000.0
        
        >>> func.ts2str(ts)
        '2020-06-27 00:00:00 GMT +0000'
        >>>

        >>> from pynoz import tz
        >>> tz.ZONES_PROMPT.Asia.Shanghai
        'Asia/Shanghai'
        >>>

        >>> func.ts2str(ts,tz='Asia/Shanghai')
        '2020-06-26 15:54:00 GMT +0806'
        >>>
        
        >>> func.ts2dt(ts,'Asia/Shanghai')
        datetime.datetime(2020, 6, 26, 15, 54, tzinfo=datetime.timezone(datetime.timedelta(0, 29160), 'GMT'))
        >>>
        


APIS
====

func
~~~~
- def dt2dict(dt):
- def dt2ts(dt):
- def detect_fmt(s):
- def dt2str(dt,fmt_or_name='YmdHMSZz'):
- def str2dt(s,fmt_or_name=None):
- def str2dict(s,fmt_or_name=None):
- def str2ts(s,fmt_or_name=None):
- def zzo2tmzone(zzo):
- def ts2dt(ts,zzo='GMT+0'):
- def ts2dict(ts,zzo='GMT+0'):
- def ts2str(ts,**kwargs):
- def dict2ts(d):
- def dict2dt(d):
- def dict2str(d,fmt_or_name='YmdHMSfZz'):

tz
~~
- def zone2z(zone):
- def zone2dict(zone):
- def utcoffset2tmzone(offset):
- def get_soffset_from_tmzone(tmzone):
- def z2offset(z):
- def z2tmzone(z):
- def zone2tmzone(zone):
- def dict2tmzone(d):

const
~~~~~

named-fmt
#########
    
    ::
        
        >>> pobj(func.FMT_TO_NAME_DICT)
        {
         '%a, %d %b %Y %H:%M:%S GMT': 'rfc1123',
         '%d %b %Y %H:%M:%S GMT': 'rfc1123_nowkday',
         '%a, %d %b %Y %H:%M:%S': 'rfc1123_notz',
         '%a, %d %b %Y %H:%M:%S %z': 'rfc1123_tzoffset',
         '%a, %d-%b-%Y %H:%M:%S GMT': 'rfc1123_hypen',
         '%A, %d-%b-%y %H:%M:%S GMT': 'rfc850',
         '%d-%b-%y %H:%M:%S GMT': 'rfc850_nowkday',
         '%a, %d-%b-%y %H:%M:%S GMT': 'rfc850_a',
         '%A, %d-%b-%Y %H:%M:%S GMT': 'rfc850_broken',
         '%d-%b-%Y %H:%M:%S GMT': 'rfc850_broken_nowkday',
         '%a, %b %d %H:%M:%S %Y': 'asctime',
         '%Y-%m-%d %H:%M:%S %z': 'iso8601',
         '%a %b %d %Y %H:%M:%S %Z%z': 'abdYHMSZz',
         '%a %b %d %Y %H:%M:%S': 'abdYHMS',
         '%Y-%m-%dT%H:%M:%S.%fZ': 'nodejs',
         '%Y-%m-%d %H:%M:%S.%f': 'YmdHMSf',
         '%Y-%m-%d %H:%M:%S.%f %Z%z': 'YmdHMSfZz',
         '%Y-%m-%d %H:%M:%S %Z %z': 'YmdHMSZz'
        }
        >>>





License
=======

- MIT
