"""Module for currency exchange
This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""
def exchange(currency_from,currency_to,amount_from ):
    """generate a URL and use it to get datas from the website"""
    d='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=x&to=y&amt=z'    
    e=d.replace('x',currency_from)
    f=e.replace('y',currency_to)
    g=f.replace('z',amount_from)
    from urllib.request import urlopen
    doc=urlopen(g)
    docstr=doc.read()
    doc.close()
    jstr=docstr.decode('ascii')
    return jstr

def test_exchange():
    """test the function 'exchange' """
    a="USD"
    b="EUR"
    c="2.5"
    t1=exchange(a,b,c)
    tt1='{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'
    assert (t1==tt1)
    a="BWP"
    b="NZD"
    c="4.73"
    t2=exchange(a,b,c)
    tt2='{ "from" : "4.73 Botswanan Pula", "to" : "0.66796788832763 New Zealand Dollars", "success" : true, "error" : "" }'
    assert (t2==tt2)
    a="CAD"
    b="CAD"
    c="10.8"
    t3=exchange(a,b,c)
    tt3='{ "from" : "10.8 Canadian Dollars", "to" : "10.8 Canadian Dollars", "success" : true, "error" : "" }'
    assert (t3==tt3)
def extract(m):
    """output the result in a proper way"""
    i=m.split('"')
    h=i[7]
    """amount and currency symbols"""
    j=h.partition(' ')
    k=j[0]
    """amount only"""
    return k
def test_extract():
    """test the function 'extract' """
    """test 1"""
    a="USD"
    b="EUR"
    c="2.5"
    t1=exchange(a,b,c)
    i1=extract(t1)
    ii1='2.1589225'
    assert (i1==ii1)
    a="BWP"
    b="NZD"
    c="4.73"
    t2=exchange(a,b,c)
    i2=extract(t2)
    ii2='0.66796788832763'
    assert (i2==ii2)
    """test 3"""
    a="CAD"
    b="CAD"
    c="10.8"
    t3=exchange(a,b,c)
    i3=extract(t3)
    ii3='10.8'
    assert (i3==ii3)
def testAll():
    """test all cases"""
    test_exchange()
    test_extract()
    print("All tests passed")
def main():
    """get the inputs, test all cases, and then output"""
    x=input()
    y=input()
    z=input()
    q=exchange(x,y,z)
    s=extract(q)
    print(s)
    testAll() 
if __name__=="__main__":
    main()
