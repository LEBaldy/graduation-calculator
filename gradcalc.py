import sys
import math
from pathlib import Path
sys.path.insert(0,str(Path().resolve())+'/packages')
from packages.gspread import authorize
from packages.oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime


#Getting input
Tau, Phi, CurrentStudents="hi", "hi", "hi"
print("Input number after e only")
while type(Tau)==str:
  Tau=input("What is your current Tau?\n")
  try:Tau=float(Tau)
  except:
    print("\nPlease input your current Tau.")
while type(Phi)==str:
  Phi=input("What is your current Phi?\n")
  try:Phi=float(Phi)
  except:
    print("\nPlease input a number for Phi.")
while type(CurrentStudents)==str:
  CurrentStudents=input("How many students do you have currently?\n")
  try:CurrentStudents=float(CurrentStudents)
  except:
    print("\nPlease input a number for students.")
print("\n")

#Additional Variable Setup
Var, FinalOutput, Ft, GradSection, UpperLimits, sigma_skips, infinite_loop, error_message, Finalput= [CurrentStudents, Tau, Phi, Phi + Tau, CurrentStudents * 200 + 1000], "N/A", "N/A", "N/A", "N/A", [144,146,149,152,155,158,161,164,166,168,172,176,180,184,188,190,193,198,203,208,213,216,218,220,224,230,236,240,242,246,248,251,254,256,261,268,275,279,282,286,289,292,296,298,304,312,316,320,324,326,328,334,336,344], False, "", ""
FtBounds = {
  #Format → (>sigma, (>Ft, <Ft), <sigma)
  #Pre-Theory
  (0, (-math.inf, 4000), 15): 4000,
  (14, (-math.inf, 4800), math.inf): 4800,
  (16, (-math.inf, math.inf), 18): 4800,
  (17, (-math.inf, math.inf), 20): 5000,
  #Theory
  (0, (5899, math.inf), 25): 6000,
  (25, (-math.inf, 7600), 25): 7600,
  (30, (-math.inf, 8200), 30): 8000,
  (0, (8899, math.inf), 40): 9000,
  #T9
  (84, (0,20100), 95): 20000,
  #R9
  (0, (13699, math.inf), 65): 14000,
  (0, (15499, 16500), 75): 16000,
  (0, (17445, 18500), 85): 18000,
  #Psi3 (190-230 skipped for R9 and T9)
  (40, (9100, 9500), 40): 9600,
  (0, (10700, 11300), 52): 11200,
  (0, (1230, 12900), 60): 12800,
  (0, (20600, 21900), 104): 21800,
  (0, (22350, 23700), 114): 23600,
  (0, (24000, 25300), 122): 25200,
  (0, (25700, 26900), 130): 26800,
  (0, (27300, 28700), 139): 28600,
  (0, (28950, 30300), 147): 30200,
  (0, (30650, 31900), 155): 31800,
  (0, (32300, 33700), 164): 33600,
  (0, (34000, 35100), 171): 35000,
  (0, (35650, 36900), 180): 36800,
  (0, (37300, 38500), 188): 38400,
  (0, (38900, 40100), 196): 40000,
  (0, (40600, 41900), 205): 41800,
  (0, (42300, 43500), 213): 43400,
  (0, (43900, 45100), 221): 45000,
  (0, (45600, 46900), 230): 46800,
  (0, (47300, 48500), 238): 48400
}

#Sheet Setup
try:
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('Encryption_Key.json', scope)
  client = authorize(creds)
  PhiTausheet, PhiTauDatasheet = client.open('Exponential Idle Average Tau*Phi (Created by Baldy)'), client.open('Exponential Idle Phi*Tau Data Collection (Created by Baldy)')
  Equations_of_Doom, Error_Collection_Grad, Data_Collection_Grad = PhiTausheet.get_worksheet(2), PhiTauDatasheet.get_worksheet(5), PhiTauDatasheet.get_worksheet(3)
except Exception as err:
  print("An error occured contacting the calculation sheet. Please contact Baldy about this. It may be due to too much traffic so try again in 10-20minutes.")
  print("\nExact Error:\n"+str(err))

def GradCalc(Tau, Phi, CurrentStudents):
  global error_message
  global FinalOutput
  global Ft
  global GradSection
  global UpperLimits
  global infinite_loop
  global Finalput
  global Ftbounds
  #Equation Calculations
  def GradSection():
    Section = "Section"
    if (Var[1] > 0):  #No Theories Check
      if (Var[0] >= 20):  #Tau under 5k Check
        if (Var[3] <= 1460):
            if (Var[0] < 25 and Var[3] < 240): Section = 277
            elif (Var[0] < 35 and Var[3] > 230 and Var[3] < 575): Section = 303
            elif (Var[0] < 40 and Var[3] > 550 and Var[3] < 730): Section = 332
            elif (Var[0] < 45 and Var[3] > 715 and Var[3] < 855): Section = 355
            elif (Var[0] < 50 and Var[3] > 845 and Var[3] < 1015): Section = 379
            elif (Var[3] > 1000 and Var[3] <= 1460): Section = 404
            else: Section = 45
        else:
          if (Var[0] >= 65):
            if (Var[0] >= 233 and Var[3] >= 6340): Section = 143
            elif (Var[3] <= 6340): 
              if (Var[0] < 75 and Var[3] < 1765): Section = 435
              elif (Var[0] <85 and Var[3] > 1750 and Var[3] < 2110): Section = 467
              elif (Var[3] > 2085 and Var[3] <= 6340): Section = 507
              else: Section = 114
            elif(Var[0] < 233):Section = "Phi*Tau too low for student count."
            else:Section = "Student Count too low for Phi*Tau. You should have 233 students or greater by now."
          else:Section = "Student Count too low for Phi*Tau. You should have R9 at ee14,000 by now."
      else:Section = "Upon reaching ee5k please respec all into Theory 1.\nIf you have no theories please input less than 20 for students."
    elif (Var[2] > 0):  #Using Students Check
      if (Var[2] < 93):  #5k Check
        if (Var[2] > 26): Section = 12  #5 student Check
        else:Section = "Phi too low for next graduation.\nPlease use !sigma or the superior !simga."
      else:Section = "Upon reaching ee5k please respec all into Theory 1.\nIf you have no theories please input 0 for tau."
    else:Section = "Are You Even Using Students?"
    
    return Section  #Outputting F(t) Section

  def R9Boost(GradMark):
    R9BoostMulti = [0, 0, 0]
    #1R9 start
    if (GradMark < 75 and 75 > Var[0] >= 65):R9BoostMulti = [GradMark / Var[0], Var[0] / 20, GradMark / 20]
    elif (75 <= GradMark < 85 and 75 > Var[0] >= 65):R9BoostMulti = [GradMark**2 / (Var[0] * 20), Var[0] / 20, (GradMark / 20)**2]
    elif (GradMark >= 85 and 75 > Var[0] >= 65):R9BoostMulti = [GradMark**3 / (Var[0] * 400), Var[0] / 20, (GradMark / 20)**3]
    #2R9 start
    elif (GradMark < 85 and 85 > Var[0] >= 75):R9BoostMulti = [GradMark**2 / Var[0]**2, (Var[0] / 20)**2, (GradMark / 20)**2]
    elif (GradMark >= 85 and 85 > Var[0] >= 75):R9BoostMulti = [GradMark**3 / (20 * Var[0]**2), (Var[0] / 20)**2,(GradMark / 20)**3]
    #3R9 start
    elif (Var[0] >= 85):R9BoostMulti = [GradMark**3 / Var[0]**3, (Var[0] / 20)**3, (GradMark / 20)**3]
    #Rounding
    R9BoostMulti = [round(R9BoostMulti[0], 3),round(R9BoostMulti[1], 3),round(R9BoostMulti[2], 3)]

    return R9BoostMulti  #Returning Boost Difference

  def FunnelSorter(GradFt, Section, Tauness, TauPerc):
    #Phi*Tau low check
    if ((GradFt - 1000) / 200 <= Var[0]):
      if Var[0] >= 20:return ["Phi*Tau too low for next graduation.", False]
      else:return ["Phi too low for next graduation.\nPlease use !sigma or the superior !simga.",False]
    elif (Var[2] < 26 and Var[0] < 20):FtOutput = ["Phi too low for next graduation.\nPlease use !sigma or the superior !simga.",False]
    #5.2→5.6 Funneling
    elif (Var[4] == 5200):FtOutput = 5600
    #Boundary Funneling
    else:
      for (sigmalb, (Ftlb, Ftub), sigmaub), Ftout in FtBounds.items():
        if sigmaub > Var[0] > sigmalb and Ftub > GradFt > Ftlb: 
          FtOutput=Ftout
          break
        FtOutput=GradFt
    
    if (FtOutput/200-5)==(Var[0]+1) and Var[0] > 142:
      for i in range(len(sigma_skips)):
        if(sigma_skips[i]==(FtOutput/200-5)):
          FtOutput+=200
    R9 = R9Boost(FtOutput / 200 - 5)

    #Outputting the F(t) for grad and R9 Boost
    return (FtOutput, R9[0], R9[1], R9[2], Tauness, TauPerc) 

  def FtCalc(Section):
    Calc, TauPerc, Tauness, attempts = False, False, False, 0
    global error_message

    def LoopTimeAlert(time, loops):
      Error_Collection_Grad.append_row(["Check loop timed out\nLoops: "+str(loops)+" loops\nTime: "+str(time)+"sec", Var[0], Var[1], Var[2], "N/A", "N/A", "N/A", "N/A", datetime.now().strftime('%Y/%m/%d %H:%M:%S'), False])
      #resetting input 
      try:Equations_of_Doom.update_cell(Section,7,"awaiting input") 
      except:pass
    Equations_of_Doom.update_cell(Section, 7,Var[3]) 
    if(Var[0]>=65):
      Equations_of_Doom.update_cell(624,4,Var[3]) #inputting to sheet
      time_start, time_current = time.time(), 0
      while (Calc == False and attempts < 50 and time_current <=120):
        #check every x seconds to see if calculator finished as to not to lag out the api
        time.sleep(0.5)  
        try:
          Calc = float(Equations_of_Doom.cell(col=8, row=Section).value)  #grabbing numbers
          TauPerc = [float(Equations_of_Doom.cell(col=5,row=624).value), float(Equations_of_Doom.cell(col=6,row=624).value), float(Equations_of_Doom.cell(col=7,row=624).value)]
          Equations_of_Doom.update_cell(Section,7,"awaiting input") #resetting input
          Equations_of_Doom.update_cell(624,4,"awaiting input")
          attempts+=1
          break
        except:
          attempts+=1
          time_current = time.time()-time_start 
          continue
      if(Calc==False):
        if(attempts>=50):
          LoopTimeAlert(time_current, attempts)
          error_message += "Potential infinite loop stopped.\nBug report has been sent for inspection.\n"
        elif(time_current >120):
          LoopTimeAlert(time_current, attempts)
          error_message += "Sheet is taking too long to respond. Please contact Baldy about this. It may be due to too much traffic so try again in 10-20minutes.\n"
        infinite_loop=True
        Ftput = [False]
      else:
        if(TauPerc[1]<TauPerc[2]):
          TauPerc[1], TauPerc[2]=TauPerc[2], TauPerc[1]
        if(TauPerc[2]>(Var[1]/Var[3])):Tauness="Low"
        elif((Var[1]/Var[3])>TauPerc[1]):Tauness="High"
        else:Tauness=True
        Ftput = FunnelSorter(Calc, Section, Tauness, TauPerc)
    else:
      time_start, time_current = time.time(), 0
      while (Calc == False and attempts <50 and time_current <=120):
        #check every x seconds to see if calculator finished as to not to lag out the api
        time.sleep(0.5)
        try:
          Calc = float(Equations_of_Doom.cell(col=8, row=Section).value) #grabbing numbers
          Equations_of_Doom.update_cell(Section,7,"awaiting input") #resetting input 
          break
        except: 
          continue
          attempts+=1
          time_current = time.time()-time_start
      if(Calc==False):
        if(attempts>=50):
          LoopTimeAlert(time_current, attempts)
          error_message += "Potential infinite loop stopped.\nBug report has been sent for inspection.\n"
        elif(time_current >120):
          LoopTimeAlert(time_current, attempts)
          error_message += "Sheet is taking too long to respond. Please contact Baldy about this. It may be due to too much traffic so try again in 10-20minutes.\n"
        infinite_loop=True
        Ftput = [False]
      else:Ftput = FunnelSorter(Calc, Section, Tauness, TauPerc)
    return Ftput

  #For Faster Calculations
  GradSection, UpperLimits = GradSection(), [int(Equations_of_Doom.cell(col=4, row=141).value),int(Equations_of_Doom.cell(col=5, row=141).value)]
  if(infinite_loop==False):
    #The Actual Output Sorter
    #Valid Input No Calculation Check
    if (Var[1] < 0 or Var[2] < 0 or Var[0] < 5):FinalOutput = str("Please Input Valid Values for Phi, Tau, and Total Students")  
    #Out of Range Check
    elif (Var[3] > UpperLimits[0] or Var[0] > UpperLimits[1]):FinalOutput = str("Values too high and outside range of equations.\nIf you have data to add please fill out https://forms.gle/myog2rNgdmQJqPsP6\nCurrent Max Supported Phi*Tau: e") + str(UpperLimits[0]) + str("\nCurrent Max Supported Students: ") + str(UpperLimits[1]) 
    elif (type(GradSection) == str):FinalOutput = GradSection  #Grad Section Error Print off
    else:  #Outputs F(t) and/or R9 Boost Based On Section
      Ft = FtCalc(GradSection)
      if (Ft[0] != False):
        #Phi*Tau low check
        if (Ft[1] == False): FinalOutput = str("Current Graduation Mark: ee") + str(Ft[0])  
        elif(2000>Ft[0] or Ft[0]>70000):apple = bounds
        #2k5k Check
        elif (Ft[1] == 0 and Ft[2] == 0 and Ft[3] == 0):FinalOutput = str("Current Graduatin Mark: ee") + str(Ft[0])  
        #5k+ Output w/ R9 Seap Check
        elif(Ft[4]==True):FinalOutput = str("Current Graduation Mark: ee") + str(Ft[0]) + str("\nTheory Income Boosted by ") + str(Ft[1]) + str("x since last Graduation.\nTheory Income Before Graduation: ") + str(Ft[2]) + str("\nTheory Income After Graduation: ") + str(Ft[3])  
        elif(Ft[4]=="High"):FinalOutput = str("Current Graduation Mark: ee") + str(Ft[0]) + str("\nTheory Income Boosted by ") + str(Ft[1]) + str("x since last Graduation.\nTheory Income Before Graduation: ") + str(Ft[2]) + str("\nTheory Income After Graduation: ") + str(Ft[3])+str("\n\nTau is high compared to Phi.\nTau Range for Phi*Tau input: ")+str(round(10**(Ft[5][2]*Var[3]-math.floor(Ft[5][2]*Var[3])),2))+str("e")+str(math.floor(Ft[5][2]*Var[3]))+str(" - ")+str(round(10**(Ft[5][1]*Var[3]-math.floor(Ft[5][1]*Var[3])),2))+str("e")+str(math.floor(Ft[5][1]*Var[3]))+str("\n\nTry to R9 seap better or begin R9 seaping.\nFor more information, check out how to R9 seap:\nhttps://exponential-idle-guides.netlify.app/guides/endgame/#push-ft-with-3r9-seapping")
        elif(Ft[4]=="Low"):FinalOutput = str("Current Graduation Mark: ee") + str(Ft[0]) + str("\nTheory Income Boosted by ") + str(Ft[1]) + str("x since last Graduation.\nTheory Income Before Graduation: ") + str(Ft[2]) + str("\nTheory Income After Graduation: ") + str(Ft[3])+str("\n\nTau is low compared to Phi.\nTau Range for Phi*Tau input: ")+str(round(10**(Ft[5][2]*Var[3]-math.floor(Ft[5][2]*Var[3])),2))+str("e")+str(math.floor(Ft[5][2]*Var[3]))+str(" - ")+str(round(10**(Ft[5][1]*Var[3]-math.floor(Ft[5][1]*Var[3])),2))+str("e")+str(math.floor(Ft[5][1]*Var[3]))+str("\n\nTry pushing theories more efficiently by using the theory simulator and corresponding guide:\nhttps://exponential-idle-guides.netlify.app/guides/theory-sim/\nAlso check out how to R9 seap:\nhttps://exponential-idle-guides.netlify.app/guides/endgame/#push-ft-with-3r9-seapping")
        else:orange=R9seaper
      else:FinalOutput=""
  else:FinalOutput = error_message

  if(type(FinalOutput)==None):
    Error_Collection_Grad.append_row([str(err), Var[0], Var[1], Var[2], "N/A", str(Ft), str(GradSection), str(UpperLimits), datetime.now().strftime('%Y/%m/%d %H:%M:%S'), False])
    return error_message+"An error occured.\nBug report has been sent for inspection."
  else:return error_message+FinalOutput
  
try:
  Gradput=GradCalc(Tau, Phi, CurrentStudents)
  print(Gradput+"\n")
  Data_Collection_Grad.append_row([Var[0], Var[1], Var[2], Gradput, datetime.now().strftime('%Y/%m/%d %H:%M:%S')])
except Exception as err:
  Error_Collection_Grad.append_row([str(err), Var[0], Var[1], Var[2], str(FinalOutput), str(Ft), str(GradSection), str(UpperLimits), datetime.now().strftime('%Y/%m/%d %H:%M:%S'), False])
  print("An error occured.\nBug report has been sent for inspection.")