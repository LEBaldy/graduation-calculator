import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time


#Getting Inputs
Tau, Phi, CurrentStudents = "hi", "hi", "hi"
while type(Tau)==str:
  Tau=input("Tau (only number after e):  ")
  if(Tau.isdigit()): Tau=int(Tau)
  else: 
    print("Please input an integer for Tau.")
    Tau="Fail"
while type(Phi)==str:
  Phi=input("Phi (only number after e):  ")
  if(Phi.isdigit()): Phi=int(Phi)
  else: 
    print("Please input an integer for Phi.")
    Phi="Fail"
while type(CurrentStudents)==str:
  CurrentStudents=input("Current Students:  ")
  if(CurrentStudents.isdigit()): CurrentStudents=int(CurrentStudents)
  else: 
    print("Please input an integer for CurrentStudents.")
    CurrentStudents="Fail"

#Grad Calc Function
def GradCalc(Tau, Phi, CurrentStudents):
    #Sheet Setup
  scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('Encryption_Key.json', scope)
  client = gspread.authorize(creds)
  sheet = client.open('Exponential Idle Average Phi (Created by Baldy)')
  Equations_of_Doom, Other_Data = sheet.get_worksheet(7), sheet.get_worksheet(8)
  
  #Additional Variable Setup
  Var, FinalOutput=[Tau, Phi, CurrentStudents, Phi+Tau, CurrentStudents*200+1000], str("Please Have Something Other Than This Output.")
  
  #Equation Calculations
  def GradSection():
      Section="Section"
      if(Var[0]>0): #No Theories Check
          if(Var[2]>=20): #Tau under 5k Check
              if(Var[3]<=int(Other_Data.cell(col=11, row=2).value)): Section=55 #Section Sorting
              else:
                  if(Var[2]>=65):
                      if(Var[2]>=233): Section=151                       
                      elif(Var[3]<=int(Other_Data.cell(col=12, row=2).value)): Section=103
                      else: Section="Phi*Tau too low for student count."                                            
                  else:
                      Section="Phi*Tau too low for student count."
          else: Section="Upon reaching ee5k please respec all into Theory 1.\nIf you have no theories please input less than 20 for students."               
      elif(Var[1]>0): #Using Students Check
          if(Var[1]<93): #5k Check
              if(Var[1]>26): Section=15 #5 student Check                
              else:Section="Phi too low for next graduation.\nPlease use !sigma or the superior !simga."     
          else: Section="Upon reaching ee5k please respec all into Theory 1.\nIf you have no theories please input 0 for tau."                  
      else: Section="Are You Even Using Students?"        
      
      return Section #Outputting F(t) Section

  def R9Boost(GradMark):
      R9BoostMulti=[0, 0, 0]
      #1R9 start
      if(GradMark<75 and 75>Var[2]>=65): R9BoostMulti=[GradMark/Var[2], Var[2]/20, GradMark/20]        
      elif(75<=GradMark<85 and 75>Var[2]>=65): R9BoostMulti=[GradMark**2/(Var[2]*20), Var[2]/20, (GradMark/20)**2]
      elif(GradMark>=85 and 75>Var[2]>=65): R9BoostMulti=[GradMark**3/(Var[2]*400), Var[2]/20, (GradMark/20)**3]
      #2R9 start    
      elif(GradMark<85 and 85>Var[2]>=75): R9BoostMulti=[GradMark**2/Var[2]**2, (Var[2]/20)**2, (GradMark/20)**2]
      elif(GradMark>=85 and 85>Var[2]>=75): R9BoostMulti=[GradMark**3/(20*Var[2]**2), (Var[2]/20)**2, (GradMark/20)**3]
      #3R9 start
      elif(Var[2]>=85): R9BoostMulti=[GradMark**3/Var[2]**3, (Var[2]/20)**3, (GradMark/20)**3]
      #Rounding
      R9BoostMulti=[round(R9BoostMulti[0], 3), round(R9BoostMulti[1],3), round(R9BoostMulti[2],3)]

      return R9BoostMulti #Returning Boost Difference
  
  def FunnelSorter(GradFt, Section):
      #Phi*Tau low check
      if((GradFt-1000)/200<=Var[2] and Var[2]>=20): return ("Phi*Tau too low for next graduation.", False)
      elif((GradFt-1000)/200<=Var[2] and Var[2]<20): return ("Phi too low for next graduation.\nPlease use !sigma or the superior !simga.", False)
      #2k5k Funneling
      elif(20>Var[2]>=18): FtOutput=5000.00
      elif(Var[1]<26): FtOutput="Phi too low for next graduation.\nPlease use !sigma or the superior !simga."
      elif(Var[2]==17): FtOutput=4800
      #5kR9 Funneling
      elif(GradFt<5300): FtOutput=5200
      elif(Var[4]==5200): FtOutput=5600
      elif(5900<=GradFt and Var[2]<25): FtOutput=6000
      elif(8900<=GradFt and Var[2]<40): FtOutput=9000
      elif(Var[2]<65 and GradFt>=13700): FtOutput=14000
      elif(9500>GradFt>9100 and Var[2]==40): FtOutput=9600 #110
      elif(11300>GradFt>10700 and 52>Var[2]): FtOutput=11200 #130            
      elif(Var[2]<60 and 12300<GradFt<12900): FtOutput=12800 #150
      #R9Psi3 Funneling
      elif(13700<=GradFt and Var[2]<65):FtOutput=14000
      elif(Var[2]<75 and 16500>GradFt>=15500): FtOutput=16000
      elif(18500>GradFt>=17450 and Var[2]<85): FtOutput=18000
      elif(Var[2]==65 and 14500>GradFt>14100): FtOutput=14400 #170
      elif(20100>GradFt and 84<Var[2]): FtOutput=20000 #230 (#190 and #210 skipped for R9 funneling)
      elif(104>Var[2] and 20600<GradFt<21900): FtOutput=21800 #250
      elif(23700>GradFt>22350 and 114>Var[2]): FtOutput=23600 #270
      elif(24000<GradFt<25300 and 122>Var[2]): FtOutput=25200 #290
      elif(130>Var[2] and 26900>GradFt>25700): FtOutput=26800 #310
      elif(Var[2]<139 and 28700>GradFt>27300): FtOutput=28600 #330
      elif(28950<GradFt<30300 and 147>Var[2]): FtOutput=30200 #350
      elif(30650<GradFt<31900 and 155>Var[2]): FtOutput=31800 #370
      elif(Var[2]<164 and 32300<GradFt<33700): FtOutput=33600 #390
      elif(171>Var[2] and 34000<GradFt<35100): FtOutput=35000 #410
      elif(180>Var[2] and 36900>GradFt>35650): FtOutput=36800 #430
      elif(188>Var[2] and 37300<GradFt<38500): FtOutput=38400 #450
      elif(40100>GradFt>38900 and 196>Var[2]): FtOutput=40000 #470
      elif(40600<GradFt<41900 and 205>Var[2]): FtOutput=41800 #490
      elif(Var[2]<213 and 43500>GradFt>42300): FtOutput=43400 #510
      elif(45100>GradFt>43900 and CurrentStudents<221): FtOutput=45000 #530
      elif(46900>GradFt>45600 and 230>Var[2]): FtOutput=46800 #550
      elif(48500>GradFt>47300 and 238>Var[2]): FtOutput=48400 #570
      else: FtOutput=GradFt
  
      if(FtOutput==str): return(FtOutput, False)
      else: R9=R9Boost(FtOutput/200-5) #R9 Boost Calculation
      
      return (FtOutput, R9[0], R9[1], R9[2]) #Outputting the F(t) for grad and R9 Boost
  
  def FtCalc(Section):
      for i in range(3): Equations_of_Doom.update_cell(Section, 4+i, Var[i]) #inputting to sheet
      Calc=False
      while(Calc==False):
          time.sleep(0.5) #check every 1 seconds to see if calculator finished as to not to lag out the api
          try:
              Calc=float(Equations_of_Doom.cell(col=8, row=Section).value) #grabbing numbers
              for i in range(3): Equations_of_Doom.update_cell(Section, 4+i, "awaiting input") #resetting input
              break
          except: continue
  
      return FunnelSorter(Calc, Section)
  
  #For Faster Calculations
  GradSection, UpperLimits=GradSection(), [int(Other_Data.cell(col=17, row=2).value),int(Other_Data.cell(col=17, row=4).value)/200-5]
  #The Actual Output Sorter
  if(Var[0]<0 or Var[1]<0 or Var[2]<5): FinalOutput=str("Please Input Valid Values for Phi, Tau, and Total Students")  #Valid Input No Calculation Check 
  elif(Var[3]>UpperLimits[0] or Var[2]>UpperLimits[1]): FinalOutput=str("Values too high and outside range of equations.\nIf you have data to add please fill out https://forms.gle/myog2rNgdmQJqPsP6\nCurrent Max Supported Phi*Tau: e")+str( UpperLimits[0])+str("\nCurrent Max Supported Students: ")+str( UpperLimits[1]) #Out of Range Check
  elif(Type(GradSection)==str): FinalOutput=GradSection #Grad Section Error Print off
  else: #Outputs F(t) and/or R9 Boost Based On Section
      Ft=FtCalc(GradSection)
      if(Ft[1]==False): FinalOutput=str(Ft[0]) #Phi*Tau low check
      elif(Ft[1]==0 and Ft[2]==0 and Ft[3]==0): FinalOutput=str("Current Graduatin Mark: ee")+str(Ft[0]) #2k5k Check
      else:FinalOutput=str("Current Graduation Mark: ee")+str(Ft[0])+str("\nTheory Income Boosted by ")+str(Ft[1])+str( "x since last Graduation.\nTheory Income Before Graduation: ")+str(Ft[2])+str("\nTheory Income After Graduaton: ")+str(Ft[3]) #5k+ Output
  
  return(FinalOutput) #Final Output
print("\n")
print(GradCalc(Tau, Phi, CurrentStudents))
