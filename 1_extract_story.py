from bs4 import BeautifulSoup
import urllib2



start_url="https://www.fictionpress.com/s/2780124/1/Rise-From-The-Ashes-OLD" #start url
end =False
split_url=start_url.split("/") 
new_url=""
for i in range(5):
    new_url=new_url+split_url[i]+"/"
i=1
while not (end):
    url=new_url+"/"+str(i)+"/"
    i=i+1
    response=urllib2.urlopen(url)
    html_text=response.read()
    response.close()

    foo=open("fiction.txt","a")##File path where you want to save this file
    soup=BeautifulSoup(html_text)

    raw_story = soup.select("div > #storytext > p ")
    if raw_story:
        title = raw_story[0].get_text()
        print title


    
        for line in raw_story:
    
            foo.write(line.get_text().encode('utf-8')+"\n")
        foo.write("\n ----><-----\n\n\n")
        
    else:
        print "<--the end-->"
        end=True
        foo.write("\n------------~~~~~~~~~--------------")
    
foo.close()


