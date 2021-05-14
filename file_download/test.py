import urllib.request

print('Beginning file download with urllib2...')

#image download url
url ="https://i0.wp.com/doublesama.com/wp-content/uploads/2019/04/That-Time-I-Got-Reincarnated-as-a-Slime.jpg"
'''url= "http://www.computersolution.tech/wp-content/uploads/2016/05/tutorialspoint-logo.png"
if url.find('/'):
    s=url.rsplit('/', 1)[1]
urllib.request.urlretrieve(url,s)'''

urllib.request.urlretrieve(url,'mkd/clcat.jpg')

import os
print (os.path.abspath("cat.jpg"))