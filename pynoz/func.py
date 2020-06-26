#y            year                  年
#m            month                 月
#d            day                   日
#h            hour                  小时
#min          minute                分
#s            second                秒
#ms           microsecond           毫秒

#ts           timestamp             整数到秒
#mts          timestamp             整数到毫秒
#tz           timezone              时区名字
#soffset       timezone-seconds-offset       时区偏移    utc + offset = local
#msoffset       timezone-microseconds-offset       时区偏移    utc + offset = local


#yq           quarter-of-year        每年第几季
#yw           week-of-year           每年第几周
#yd           day-of-year            每年第几天


#qm           month-of-quarter        每季第几月
#qw           week-of-quarter         每季第几周
#qd           day-of-quarter          每季第几天

#mt           ten-of-month            每月第几旬
#mw           week-of-month           每月第几周


#wd           weekday                 星期几


#dt           daytime


import time
from datetime import datetime,timedelta,timezone
import pytz
import calendar
from pynoz.tz import zone2dict,ZONES_Z_MD 
from datetime import date as datetme_date

DICT_KL = ['y', 'm', 'd', 'h', 'min', 's', 'ms', 'ts', 'mts', 'tzname', 'soffset', 'msoffset', 'yq', 'yw', 'yd', 'qm', 'qw', 'qd', 'mt', 'mw', 'td', 'wd']


DATE_FMT = [
    
]



def get_yq_via_m(m):
    m = m -1
    return((m - m % 3)//3+1)

def get_days_num_of_year(y):
    cond = calendar.isleap(y)
    return(366 if(cond) else 365)

def get_yw(y,m,d):
    date = datetme_date(y,m,d)
    t = date.isocalendar()
    return(t[1])


def get_days_num_of_month(y,m):
    t = calendar.monthrange(y,m)
    return(t[1])

def get_yd(y,m,d):
    '''
        from 1 to 365/266
    '''
    yd = 0 
    for i in range(1,m):
        yd = yd + get_days_num_of_month(y,m)
    yd = yd + d
    return(yd)

def get_qm(m):
    return(m%3 if(m%3) else 3)

def get_fst_date_of_q(y,q):
    if(q==1):
        return(datetme_date(y,1,1))
    elif(q==2):
        return(datetme_date(y,4,1))
    elif(q==3):
        return(datetme_date(y,7,1))
    else:
        return(datetme_date(y,10,1))


def get_qw(y,q,m,d):
    fst_date = get_fst_date_of_q(y,q)
    fst_yw = fst_date.isocalendar()[1]
    yw = get_yw(y,m,d)
    qw = 1 + (yw - fst_yw)
    return(qw)


def get_qd(y,q,m,d):
    fst_date = get_fst_date_of_q(y,q)
    fst_yd = get_yd(fst_date.year,fst_date.month,fst_date.day)
    yd = get_yd(y,m,d)
    qd = 1 + (yd - fst_yd)
    return(qd)


def get_mt(m,d):
    if(d>=1 and d<=10):
        return(1)
    elif(d>=10 and d<=20):
        return(2)
    else:
        return(3)


def get_fst_date_of_m(y,m):
    return(datetme_date(y,m,1))


def get_mw(y,m,d):
    fst_date = get_fst_date_of_m(y,m)
    fst_yw = fst_date.isocalendar()[1]
    yw = get_yw(y,m,d)
    mw = 1 + (yw - fst_yw)
    return(mw)


def get_td(y,m,d):
    t = get_mt(m,d)
    if(t == 1):
        return(d)
    elif(t ==2):
        return(d-10)
    else:
        return(d-20)



def dt2dict(dt):
    global DICT_KL
    y = dt.year
    m = dt.month 
    d = dt.day 
    h = dt.hour
    min = dt.minute
    s = dt.second
    ms = dt.microsecond * 1000
    ts = dt.timestamp()
    mts = ts * 1000
    tzname = dt.tzname()
    z = dt.strftime('%z')
    zone = ZONES_Z_MD[z] if(z!='+0000') else 'GMT'
    delta = dt.utcoffset()
    soffset = delta.total_seconds()
    msoffset =  soffset * 1000
    yq = get_yq_via_m(m)
    date = dt.date()
    yw = date.isocalendar()[1]
    yd = get_yd(y,m,d)
    qm = get_qm(m)
    qw = get_qw(y,yq,m,d)
    qd = get_qd(y,yq,m,d)
    mt = get_mt(m,d)
    mw = get_mw(y,m,d)
    td = get_td(y,m,d)
    wd = dt.weekday()
    d = {
        "y":y,
        "m":m, 
        "d":d,
        "h":h,
        "min":min,
        "s":s,
        "ms":ms,
        "ts":ts,
        "mts":mts,
        "z":z,
        "zone":zone,
        "tzname":tzname,
        "soffset":soffset,
        "msoffset":msoffset,
        "yq":yq,
        "yw":yw,
        "yd":yd,
        "qm":qm,
        "qw":qw,
        "qd":qd,
        "mt":mt,
        "mw":mw,
        "td":td,
        "wd":wd,
    }
    return(d)

def dt2ts(dt):
    return(dt.timestamp())

#dt2str
#

#str2dict
#str2dt
#str2ts

#ts2dict
#ts2dt
#ts2str


