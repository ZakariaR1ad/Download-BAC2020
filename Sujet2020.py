from math import e
import urllib.request
import requests
import os
from pathlib import Path
import shutil




modules = ["arabic", "french", "english", "math", "sciences", "philosophy","hisgeo","physics"]
modules_spe = ["german","electric","spanish","g_civil", "islamic","g_mecanique","g_procedes","gestion","economy","amazigh"]
fields = ["sci", "le", "lp","m","lit","mt","se"]
year = 2020
for module in modules:
    for field in fields:
            
        folder_name = str(module)+"/"+str(field)
        if not os.path.exists("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\"+folder_name):
            os.makedirs("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\"+folder_name)
        url_sujet = "https://www.ency-education.com/uploads/3/0/9/3/309326/"+str(module)+"-"+str(field)+"-bac"+str(year)+".pdf"
        url_corr = "https://www.ency-education.com/uploads/3/0/9/3/309326/"+str(module)+"-"+str(field)+"-bac"+str(year)+"-correction"+".pdf"
        try:
            r = requests.get(url_sujet, allow_redirects=True, stream=True)

            if(r.headers['Content-Type']=="application/pdf"):
                with open(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name,"sujet.pdf"), "wb") as pdf:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            pdf.write(chunk)
                    pdf.close()
            r = requests.get(url_corr, allow_redirects=True, stream=True)
            if(r.headers['Content-Type']=="application/pdf"):
                with open(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name,"correction.pdf"), "wb") as pdf:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            pdf.write(chunk)
                    pdf.close()

            if len(os.listdir(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name))) == 0: # Check if the folder is empty
                    shutil.rmtree(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name))
            else:
                print("ok")
            
        except:
            print("no such url", url_sujet)
            try:

                url_sujet = "https://www.ency-education.com/uploads/3/0/9/3/309326/"+str(module)+"-"+str(field)+"-bac"+str(year)+".jpeg"
                url_corr = "https://www.ency-education.com/uploads/3/0/9/3/309326/"+str(module)+"-"+str(field)+"-bac"+str(year)+"-correction"+".jpeg"

                folder_name = str(module)+"/"+str(year)+"/"+str(field)
                if not os.path.exists("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\"+folder_name):
                    os.makedirs("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\"+folder_name)
                r = requests.get(url_sujet, allow_redirects=True, stream=True)
                if(r.headers['Content-Type']=="image"):
                    with open(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name,"sujet.jpeg"), "wb") as pdf:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:
                                pdf.write(chunk)
                        pdf.close()
                if(r.headers['Content-Type']=="image"):
                    r = requests.get(url_corr, allow_redirects=True, stream=True)
                    with open(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name,"correction.jpeg"), "wb") as pdf:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:
                                pdf.write(chunk)
                        pdf.close()
                if len(os.listdir(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name))) == 0: # Check if the folder is empty
                    shutil.rmtree(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name))
                else:
                    print("ok")
            except:
                print("no such url", url_sujet)
for module in modules_spe:

    try:
        folder_name = str(module)+"/"+str(year)
        if not os.path.exists("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\"+folder_name):
                os.makedirs("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\"+folder_name)
        
        url_sujet = "https://www.ency-education.com/uploads/3/0/9/3/309326/"+str(module)+"-bac"+str(year)+".pdf"
        url_corr = "https://www.ency-education.com/uploads/3/0/9/3/309326/"+str(module)+"-bac"+str(year)+"-correction"+".pdf"
        r = requests.get(url_sujet, allow_redirects=True, stream=True)
        if(r.headers['Content-Type']=="application/pdf"):
            
            with open(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name,"sujet.pdf"), "wb") as pdf:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:
                                pdf.write(chunk)
                        pdf.close()
        if(r.headers['Content-Type']=="application/pdf"):
            r = requests.get(url_corr, allow_redirects=True, stream=True)
            with open(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name,"correction.pdf"), "wb") as pdf:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:
                                pdf.write(chunk)
                        pdf.close()
        if len(os.listdir(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name))) == 0: # Check if the folder is empty
                    shutil.rmtree(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name))
        else:
            print("ok")
        

    except:
        print("no such url", url_sujet)
        
        try:
            url_sujet = "https://www.ency-education.com/uploads/3/0/9/3/309326/"+str(module)+"-bac"+str(year)+".jpeg"
            url_corr = "https://www.ency-education.com/uploads/3/0/9/3/309326/"+str(module)+"-bac"+str(year)+"-correction"+".jpeg"
            folder_name = str(module)+"/"+str(field)
            if not os.path.exists("C:\\Users\\assas\\OneDrive\\Documents\\Bac"+folder_name):
                os.makedirs("C:\\Users\\assas\\OneDrive\\Documents\\Bac"+folder_name)
            r = requests.get(url_sujet, allow_redirects=True, stream=True)
            if(r.headers['Content-Type']=="image"):
                with open(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name,"sujet.jpeg"), "wb") as pdf:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:
                                pdf.write(chunk)
                        pdf.close()
            if(r.headers['Content-Type']=="image"):
                r = requests.get(url_corr, allow_redirects=True, stream=True)
                with open(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name,"correction.jpeg"), "wb") as pdf:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:
                                pdf.write(chunk)
                        pdf.close()
            if len(os.listdir(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name))) == 0: # Check if the folder is empty
                    shutil.rmtree(os.path.join("C:\\Users\\assas\\OneDrive\\Documents\\Bac\\",folder_name))
            else:
                print("ok")
        except:
            print("no such url", url_sujet)
            
            

