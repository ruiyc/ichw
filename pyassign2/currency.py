"""Module for currency exchange
This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""
def get(a,b,c):
    """generate a URL to be used later"""
    d='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=currency_from&to=currency_to&amt=amount_from'    
    e=d.replace('currency_from',a)
    f=e.replace('currency_to',b)
    g=f.replace('amount_from',c)
    return g
def test_get():
    """test the function 'get' """
    a="USD"
    b="EUR"
    c="2.5"
    d1=get(a,b,c)
    dd1='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5'
    assert (d1==dd1)
    a="BWP"
    b="NZD"
    c="4.73"
    d2=get(a,b,c)
    dd2='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=BWP&to=NZD&amt=4.73'
    assert (d2==dd2)
    a="CAD"
    b="CAD"
    c="10.8"
    d3=get(a,b,c)
    dd3='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=CAD&to=CAD&amt=10.8'
    assert (d3==dd3)
def exchange(d):
    """use the URL to get datas from the website"""
    from urllib.request import urlopen
    doc=urlopen(d)
    docstr=doc.read()
    doc.close()
    jstr=docstr.decode('ascii')
    return jstr
def test_exchange():
    """test the function 'exchange' """
    a="USD"
    b="EUR"
    c="2.5"
    d1=get(a,b,c)
    t1=exchange(d1)
    tt1='{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'
    assert (t1==tt1)
    a="BWP"
    b="NZD"
    c="4.73"
    d2=get(a,b,c)
    t2=exchange(d2)
    tt2='{ "from" : "4.73 Botswanan Pula", "to" : "0.66796788832763 New Zealand Dollars", "success" : true, "error" : "" }'
    assert (t2==tt2)
    a="CAD"
    b="CAD"
    c="10.8"
    d3=get(a,b,c)
    t3=exchange(d3)
    tt3='{ "from" : "10.8 Canadian Dollars", "to" : "10.8 Canadian Dollars", "success" : true, "error" : "" }'
    assert (t3==tt3)
def extract(e):
    """output the result in a proper way"""
    i=e.split('"')
    h=i[7]"""amount + currency symbol"""
    j=h.partition(' ')
    k=j[0]"""amount only"""
    return k
def test_extract():
    """test the function 'extract' """
    """test 1"""
    a="USD"
    b="EUR"
    c="2.5"
    d1=get(a,b,c)
    t1=exchange(d1)
    i1=extract(t1)
    ii1='2.1589225'
    assert (i1==ii1)
    a="BWP"
    b="NZD"
    c="4.73"
    d2=get(a,b,c)
    t2=exchange(d2)
    i2=extract(t2)
    ii2='0.66796788832763'
    assert (i2==ii2)
    """test 3"""
    a="CAD"
    b="CAD"
    c="10.8"
    d3=get(a,b,c)
    t3=exchange(d3)
    i3=extract(t3)
    ii3='10.8'
    assert (i3==ii3)
def testAll():
    """test all cases"""
    test_get()
    test_exchange()
    test_extract()
    print("All tests passed")
def main():
    """get the inputs, test all cases, and then output"""
    x=input()
    y=input()
    z=input()
    p=get(x,y,z)
    q=exchange(p)
    s=extract(q)
    print(s)
    testAll() 
if __name__=="__main__":
    main()
