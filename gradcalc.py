import sys
from pathlib import Path
sys.path.insert(0,str(Path().resolve())+'/packages')
from packages.gspread import authorize
from packages.oauth2client.service_account import ServiceAccountCredentials
import time

#Getting input
Tau, Phi, CurrentStudents="hi", "hi", "hi"
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
def GradCalc(Tau, Phi, CurrentStudents):

  #Additional Variable Setup
  Var, FinalOutput, Ft, GradSection, UpperLimits, sigma_skips, infinite_loop, error_message, Finalput= [CurrentStudents, Tau, Phi, Phi + Tau, CurrentStudents * 200 + 1000], "N/A", "N/A", "N/A", "N/A", [166, 190, 216, 220, 240, 246, 251, 256, 272, 279, 298, 307, 310, 316, 324, 326, 334], False, "", ""

  #Sheet Setup
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('Encryption_Key.json', scope)
  client = authorize(creds)
  sheet = client.open('Exponential Idle Average Tau*Phi (Created by Baldy)')
  Equations_of_Doom, Error_Collection_Grad = sheet.get_worksheet(5), sheet.get_worksheet(6)

  try:
    #Grad Calc Function
    def GraduationCalc(Tau, Phi, CurrentStudents):
      Var, FinalOutput, Ft, GradSection, UpperLimits, sigma_skips, infinite_loop, error_message, Finalput= [CurrentStudents, Tau, Phi, Phi + Tau, CurrentStudents * 200 + 1000], "N/A", "N/A", "N/A", "N/A", [166, 190, 216, 220, 240, 246, 251, 256, 272, 279, 298, 307, 310, 316, 324, 326, 334], False, "", ""
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
                else:Section = "Studnt Count too low for Phi*Tau."
              else:Section = "Student Count too low for Phi*Tau."
          else:Section = "Upon reaching ee5k please respec all into Theory 1.\nIf you have no theories please input less than 20 for students."
        elif (Var[2] > 0):  #Using Students Check
          if (Var[2] < 93):  #5k Check
            if (Var[2] > 26): Section = 12  #5 student Check
            else:Section = "Phi too low for next graduation.\nPlease use !sigma or the superior !simga."
          else:Section = "Upon reaching ee5k please respec all into Theory 1.\nIf you have no theories please input 0 for tau."
        else:Section = "Are You Even Using Students?"
        
        return Section  #Outputting F(t) Section

      def R9Seaper(GradMark):


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

      def FunnelSorter(GradFt, Section, TauPerc):
        try:
          if(TauPerc[2]>(Var[1]/Var[3])):Tauness="Low"
          elif((Var[1]/Var[3])>TauPerc[1]):Tauness="High"
          else:Tauness=True
        except Exception as err:Tauness=True
        #Phi*Tau low check
        if ((GradFt - 1000) / 200 <= Var[0] and Var[0] >= 20):return ("Phi*Tau too low for next graduation.", False)
        elif ((GradFt - 1000) / 200 <= Var[0] and Var[0] < 20):return ("Phi too low for next graduation.\nPlease use !sigma or the superior !simga.",False)
        #2k5k Funneling
        elif (20 > Var[0] >= 18):FtOutput = 5000.00
        elif (Var[2] < 26 and Var[0] < 20):FtOutput = "Phi too low for next graduation.\nPlease use !sigma or the superior !simga."
        elif (Var[0] == 17):FtOutput = 4800
        #5kR9 Funneling
        elif ((GradFt < 5300 or Var[3] <= 120) and Var[0]==20):FtOutput = 5200
        elif (Var[4] == 5200):FtOutput = 5600
        elif (5900 <= GradFt and Var[0] < 25):FtOutput = 6000
        elif (8900 <= GradFt and Var[0] < 40):FtOutput = 9000
        elif (Var[0] < 65 and GradFt >= 13700):FtOutput = 14000
        elif (9500 > GradFt > 9100 and Var[0] == 40):FtOutput = 9600  #110
        elif (11300 > GradFt > 10700 and 52 > Var[0]):FtOutput = 11200  #130
        elif (Var[0] < 60 and 12300 < GradFt < 12900):FtOutput = 12800  #150
        #R9Psi3 Funneling
        elif (13700 <= GradFt and Var[0] < 65):FtOutput = 14000
        elif (Var[0] < 75 and 16500 > GradFt >= 15500):FtOutput = 16000
        elif (18500 > GradFt >= 17450 and Var[0] < 85):FtOutput = 18000
        elif (Var[0] == 65 and 14500 > GradFt > 14100):FtOutput = 14400  #170
        elif (20100 > GradFt and 84 < Var[0]):FtOutput = 20000  #230 (#190 and #210 skipped for R9 funneling)
        elif (104 > Var[0] and 20600 < GradFt < 21900):FtOutput = 21800  #250
        elif (23700 > GradFt > 22350 and 114 > Var[0]):FtOutput = 23600  #270
        elif (24000 < GradFt < 25300 and 122 > Var[0]):FtOutput = 25200  #290
        elif (130 > Var[0] and 26900 > GradFt > 25700):FtOutput = 26800  #310
        elif (Var[0] < 139 and 28700 > GradFt > 27300):FtOutput = 28600  #330
        elif (28950 < GradFt < 30300 and 147 > Var[0]):FtOutput = 30200  #350
        elif (30650 < GradFt < 31900 and 155 > Var[0]):FtOutput = 31800  #370
        elif (Var[0] < 164 and 32300 < GradFt < 33700):FtOutput = 33600  #390
        elif (171 > Var[0] and 34000 < GradFt < 35100):FtOutput = 35000  #410
        elif (180 > Var[0] and 36900 > GradFt > 35650):FtOutput = 36800  #430
        elif (188 > Var[0] and 37300 < GradFt < 38500):FtOutput = 38400  #450
        elif (40100 > GradFt > 38900 and 196 > Var[0]):FtOutput = 40000  #470
        elif (40600 < GradFt < 41900 and 205 > Var[0]):FtOutput = 41800  #490
        elif (Var[0] < 213 and 43500 > GradFt > 42300):FtOutput = 43400  #510
        elif (45100 > GradFt > 43900 and CurrentStudents < 221):FtOutput = 45000  #530
        elif (46900 > GradFt > 45600 and 230 > Var[0]):FtOutput = 46800  #550
        elif (48500 > GradFt > 47300 and 238 > Var[0]):FtOutput = 48400  #570
        elif (GradFt < 8200 and 30 == Var[0]):FtOutput = 8000
        elif(GradFt < 7600 and 25 == Var[0]):FtOutput = 7600
        else:FtOutput = GradFt

        if((FtOutput/200-5)==(Var[2]+1)):
          for i in range(len(sigma_skips)):
            if(sigma_skips[i]==(FtOutput/200-5)):
              FtOutput+=200
        if (type(FtOutput) == str): return (FtOutput, False)
        else: R9 = R9Boost(FtOutput / 200 - 5)  #R9 Boost Calculation

        return (FtOutput, R9[0], R9[1], R9[2), Tauness)  #Outputting the F(t) for grad and R9 Boost

      def FtCalc(Section):
        Calc, TauPerc, attempts = False, 0
        if(Var[0]>=65):
          for i in range(3):
            Equations_of_Doom.update_cell(Section, 4 + i,Var[i])  
          Equations_of_Doom.update_cell(622,4,Var[3]) #inputting to sheet
          while (Calc == False and attempts <50):
            time.sleep(0.5)  #check every 1 seconds to see if calculator finished as to not to lag out the api
            try:
              Calc = float(Equations_of_Doom.cell(col=8, row=Section).value)  #grabbing numbers
              TauPerc = [float(Equations_of_Doom.cell(col=5,row=622).value), float(Equations_of_Doom.cell(col=6,row=622).value), float(Equations_of_Doom.cell(col=7,row=622).value)]
              for i in range(3):Equations_of_Doom.update_cell(Section, 4 + i, "awaiting input")  #resetting input
              Equations_of_Doom.update_cell(622, 4, "awaiting input")
              break
            except: continue
            attempts+=1
          if(attempts>=50 and Calc==False):
            Error_Collection_Grad.append_row(["Check Loop Timed Out", Ft, "N/A","N/A","N/A","N/A","N/A","N/A", FinalOutput, FtSection, UpperLimit])
            error_message += "Potential infinite loop stopped.\nBug report has been sent for inspection. Status can be found here:\nhttps://bit.ly/3qOu0mn\n\n"
            infinite_loop=True
            Ftput = False
          else:Ftput = FunnelSorter(Calc, Section, TauPerc)
        else:
          for i in range(3):
            Equations_of_Doom.update_cell(Section, 4 + i,Var[i])  #inputting to sheet
          while (Calc == False and attempts <50):
            time.sleep(0.5)  #check every 1 seconds to see if calculator finished as to not to lag out the api
            try:
              Calc = float(Equations_of_Doom.cell(col=8, row=Section).value)  #grabbing numbers
              for i in range(3):Equations_of_Doom.update_cell(Section, 4 + i, "awaiting input")  #resetting input
              break
            except: continue
            attempts+=1
          if(attempts>=50 and Calc==False):
            Error_Collection_Grad.append_row(["Check Loop Timed Out", Ft, "N/A","N/A","N/A","N/A","N/A","N/A", FinalOutput, FtSection, UpperLimit])
            error_message += "Potential infinite loop stopped.\nBug report has been sent for inspection. Status can be found here:\nhttps://bit.ly/3qOu0mn\n\n"
            infinite_loop=True
            Ftput = False
          else:Ftput = FunnelSorter(Calc, Section, TauPerc)
        return Ftput

      #For Faster Calculations
      GradSection, UpperLimits = GradSection(), [int(Equations_of_Doom.cell(col=4, row=141).value),int(Equations_of_Doom.cell(col=5, row=141).value)]
      try:
        if(infinite_loop==False):
          #The Actual Output Sorter
          if (Var[1] < 0 or Var[2] < 0 or Var[0] < 5):FinalOutput = str("Please Input Valid Values for Phi, Tau, and Total Students")  #Valid Input No Calculation Check
          elif (Var[3] > UpperLimits[0] or Var[0] > UpperLimits[1]):FinalOutput = str("Values too high and outside range of equations.\nIf you have data to add please fill out https://forms.gle/myog2rNgdmQJqPsP6\nCurrent Max Supported Phi*Tau: e") + str(UpperLimits[0]) + str("\nCurrent Max Supported Students: ") + str(UpperLimits[1])  #Out of Range Check
          elif (type(GradSection) == str):FinalOutput = GradSection  #Grad Section Error Print off
          else:  #Outputs F(t) and/or R9 Boost Based On Section
            Ft = FtCalc(GradSection)
            if (Ft[1] == False): FinalOutput = str("Current Graduation Mark: ee") + str(Ft[0])  #Phi*Tau low check
            elif(2000>Ft[0] or Ft[0]>60000):apple = bounds
            elif (Ft[1] == 0 and Ft[2] == 0 and Ft[3] == 0):FinalOutput = str("Current Graduatin Mark: ee") + str(Ft[0])  #2k5k Check
            elif(Ft[4]==True):FinalOutput = str("Current Graduation Mark: ee") + str(Ft[0]) + str("\nTheory Income Boosted by ") + str(Ft[1]) + str("x since last Graduation.\nTheory Income Before Graduation: ") + str(Ft[2]) + str("\nTheory Income After Graduation: ") + str(Ft[3])  #5k+ Output w/ R9 Seap Check
            elif(Ft[4]="High"):FinalOutput = str("Tau is high compared to Phi. Try to R9 seap better or begin R9 seaping. For more information, check out how to R9 seap:\nhttps://exponential-idle-guides.netlify.app/guides/endgame/#push-ft-with-3r9-seapping\n\nCurrent Graduation Mark: ee") + str(Ft[0]) + str("\nTheory Income Boosted by ") + str(Ft[1]) + str("x since last Graduation.\nTheory Income Before Graduation: ") + str(Ft[2]) + str("\nTheory Income After Graduation: ") + str(Ft[3])
            elif(Ft[4]="Low"):FinalOutput = str("Tau is low compared to Phi. Try pushing theories more efficiently by using the theory simulator and corresponding guide:\nhttps://exponential-idle-guides.netlify.app/guides/theory-sim/\nAlso check out how to R9 seap:\nhttps://exponential-idle-guides.netlify.app/guides/endgame/#push-ft-with-3r9-seapping\n\nCurrent Graduation Mark: ee") + str(Ft[0]) + str("\nTheory Income Boosted by ") + str(Ft[1]) + str("x since last Graduation.\nTheory Income Before Graduation: ") + str(Ft[2]) + str("\nTheory Income After Graduation: ") + str(Ft[3])
            else:orange=R9seaper
        else:FinalOutput = error_message

        return (FinalOutput)  #Final Output
      except Exception as err:
        pass
        Error_Collection_Grad.append_row([str(err), Var[0], Var[1], Var[2], FinalOutput, Ft, GradSection, UpperLimits])
        error_message += "An error occured.\nBug report has been sent for inspection. Status can be found here:\nhttps://bit.ly/3qOu0mn\n\n"
    Calcput=GraduationCalc(Tau, Phi, CurrentStudents)
    if(type(Calcput)==None):
      Error_Collection_Grad.append_row([str(err), Var[0], Var[1], Var[2], FinalOutput, Ft, GradSection, UpperLimits])
      error_message += "An error occured.\nBug report has been sent for inspection. Status can be found here:\nhttps://bit.ly/3qOu0mn\n\n"
    else:Finalput = str(Calcput)
  except Exception as err:
    pass
    Error_Collection_Grad.append_row([str(err), Var[0], Var[1], Var[2], FinalOutput, Ft, GradSection, UpperLimits])
    print("An error occured.\nBug report has been sent for inspection. Status can be found here:\nhttps://bit.ly/3qOu0mn\n\n")

  
  return error_message+Finalput

try:print(GradCalc(Tau, Phi, CurrentStudents))
except Exception as err:
  pass
  Error_Collection_Grad.append_row([str(err), Var[0], Var[1], Var[2], FinalOutput, Ft, GradSection, UpperLimits])
  print("An error occured.\nBug report has been sent for inspection. Status can be found here:\nhttps://bit.ly/3qOu0mn\n\n")