import cherrypy
import sys
import numpy as np 
from random import *


class Server:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''
        
        body = cherrypy.request.json
        #self.coup_possible(body)
        self.player(body)
        #print(body)
        #self.liste=np.array(body["game"])
        #self.tableau=self.liste.reshape(5,5)
        #print(self.tableau)
        return {"move": self.jouer_coup(body),"message":"I m smart"}

    def player(self,body):#je joue les croix ou les ronds ? 
        if body["players"][0]==body["you"]:
            joueur=0
        if body["players"][1]==body["you"]:
            joueur=1
        return joueur 

    def coup_possible(self, body):#quel coup est t-il possible de jouer suivant l etat du jeu ?
        
        listepos2=[]
        listeindice=[0,1,2,3,4,5,9,10,14,15,19,20,21,22,23,24]

        if self.player(body) == 0 :
            listepos2=[]
            for i in range(0, len(body["game"])):
                value = body["game"][i]
                if value == 0 and i in listeindice:
                    listepos2.append([i])
                if value == None and i in listeindice :
                     listepos2.append([i])
                if value == 1 and i in listepos2:
                    listepos2.remove(i)
        
            

        if self.player(body) == 1 :
            listepos2=[]
            for i in range(0, len(body["game"])):
                value = body["game"][i]
                if value == 1 and i in listeindice:
                    listepos2.append([i])
                if value == None and i in listeindice :
                    listepos2.append([i])
                if value == 0 and i in listepos2:
                    listepos2.remove(i)

        return listepos2

        #if self.joueur == 1:
             #for elem in body["game"]:
                #if elem == 1:
                    #self.listepos2.append([elem])
                #if elem ==None:
                    #self.listepos2.append([elem])
            #return self.listepos2

    



    def jouer_coup(self,body):#c est cette fonction qui renvoie le coup jouer 
        case = choice(self.coup_possible(body))
        case1=case[0]
        liste1=[0,1,2,3,4]
        liste2=[0,5,10,15,20]
        liste3=[4,9,14,19,24]
        liste4=[20,21,22,23,24]
        liste5=[1,6,11,16,21]
        liste6=[2,7,12,17,22]
        liste7=[3,8,13,18,23]
        liste8=[5,6,7,8,9]
        liste9=[10,11,12,13,14]
        liste10=[15,16,17,18,19]
        totalcroix1=0
        totalcroix2=0
        direction2=""
        if self.player(body)==0:
            if case1==0:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste2:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="E"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==1:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste5:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="E"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==2:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste6:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="E"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==3:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste7:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="E"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==4:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste3:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==5:
                for i in liste2:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste8:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="E"

            if case1==9:
                for i in liste3:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste8:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="W"

            if case1==10:
                for i in liste2:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste9:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="E"

            if case1==14:
                for i in liste3:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste9:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="S"

                if totalcroix2> totalcroix1:
                    direction2="W"
            if case1==15:
                for i in liste2:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste10:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="E"

            if case1==19:
                for i in liste3:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste10:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="N"

            if case1==20:
                for i in liste2:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste4:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="E"

            if case1==21:
                for i in liste4:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste5:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="N"

            if case1==22:
                for i in liste4:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste6:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="N"
            if case1==23:
                for i in liste4:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste7:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="N"

            if case1==24:
                for i in liste3:
                    value2=body["game"][i]
                    if value2==0:
                        totalcroix1+=1

                for i in liste4:
                    value3=body["game"][i]
                    if value3==0:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="W"

        if self.player(body)==1:
            if case1==0:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste2:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="E"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==1:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste5:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="E"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==2:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste6:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="E"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==3:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste7:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="E"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==4:
                for i in liste1:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste3:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="S"

            if case1==5:
                for i in liste2:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste8:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="E"

            if case1==9:
                for i in liste3:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste8:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="W"

            if case1==10:
                for i in liste2:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste9:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="E"

            if case1==14:
                for i in liste3:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste9:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="S"

                if totalcroix2> totalcroix1:
                    direction2="W"
            if case1==15:
                for i in liste2:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste10:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="E"

            if case1==19:
                for i in liste3:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste10:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="N"

            if case1==20:
                for i in liste2:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste4:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="E"

            if case1==21:
                for i in liste4:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste5:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="N"

            if case1==22:
                for i in liste4:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste6:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="N"
            if case1==23:
                for i in liste4:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste7:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="W"

                if totalcroix2> totalcroix1:
                    direction2="N"

            if case1==24:
                for i in liste3:
                    value2=body["game"][i]
                    if value2==1:
                        totalcroix1+=1

                for i in liste4:
                    value3=body["game"][i]
                    if value3==1:
                        totalcroix2+=1

                if totalcroix1>= totalcroix2:
                    direction2="N"

                if totalcroix2> totalcroix1:
                    direction2="W"

        
        return {"cube":case1,"direction":direction2}












        


    


            
        

            



    
    
    
    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080

    cherrypy.config.update({'server.socket_port': port,"server.socket_host":"0.0.0.0"})
    cherrypy.quickstart(Server())