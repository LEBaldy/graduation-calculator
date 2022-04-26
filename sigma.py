import math
def sigmainputs():
  while type(tin)==str:
    tin=input("What is your current t? (x.xxe+X)\n")
    try:
      if tin>0:tin=float(tin)
      else:print("\nPlease input your current t.")
    except:
      print("\nPlease input your current t.")
  while type(starsin)==str:
    starsin=input("What is your current stars? (x.xxe+X)\n")
    try:
      if tin>0:starsin=int(starsin)
      else:print("\nPlease input your current stars.")
    except:
      print("\nPlease input your current stars.")
  while type(accelin)==str:
    accelin=input("What is your current accel? (2.85x if unknown)\n")
    try:
      if accelin <1 or accelin >= 3.18:print("\nPlease input your current accel.")
      else: accelin=float(accelin)
    except:
      print("\nPlease input your current accel.")
  while type(adbool)==bool:
    adbool=input("Are you using ad bonus? (True or False)\n")
    try:
      if adbool=="false" or adbool=="true":adbool.capitalize()
      adbool=float(adbool)
    except:
      print("\nPlease type in True or False.")
  return (tin, starsin, accelin, adbool)

def sigma(sigma, ft, otherinputs):
  t, stars, acceleration, ad = otherinputs
  if acceleration==2.85:acceleration=2.85380860601
  adbonus= 1.5 if ad else 1
  log10dmu=ft
  log10db= ft * 0.8 + math.log10(4e6)
  log10dpsi= (ft / 25 - 1) * math.log10(2)
  dtSpeed = (ft / (15.0*math.log10(2)) + 0.1) / 10
  dtLevels = ft / math.log10(4)
  dt = dtSpeed * dtLevels * adbonus * acceleration
  vals=[
    math.log10(dt),
    0.7 * math.log10(1+t),
    math.log10(1+stars),
    log10db / (10 * (log10db**0.5)),
    log10dmu / 1300.00,
    log10dpsi / 225 * log10dpsi**0.5,
  ]
  levels, maxLevels=[0,0,0,0,0,0,0], [99,99,99,8,8,8,6]
  sigma, curSum, history, REFUND_CNT=sigma-55, 0, [], 5


  def researchCost(num):return num//2 + 1
  def getCost(num):
    if num % 2 == 1: 
      return (num**2 - 1) / 4 + (num + 1) / 2
    return (num**2 + 2 * num) / 4
  def getCostOrder(order):
    return 2*order[6]+sum([getCost(order[i]) for i in range(len(order)-1)])
  def getTotalBoost(order):
    return (1 + order[6]*vals[6])*sum([order[i]*vals[i] for i in range(len(order)-1)])

  while True:
    cand, cval=None, 0
    for i in range(7):
      if levels[i] >= maxLevels[i]: continue
      cost=2 if i==6 else researchCost(levels[i])
      curval=curSum/20 if i==6 else vals[i]/cost
      if curval > cval:
        cand=i if cost <= sigma else None
        cval = curval
    
    if cand == None:break
    history.append(cand)
    if cand==6:
      sigma-=2
    else:
      curSum+= vals[cand]
      sigma-= researchCost(levels[cand])
    levels[cand]+=1
  
  for i in range(REFUND_CNT):
    if len(history)==0:break
    lastbest = history.pop()
    levels[lastbest]-=1
    if lastbest ==6:
      sigma+=2
    else:
      sigma+=researchCost(levels[lastbest])
      curSum -= vals[lastbest]
  
  def search(i, sigma, curSum):
    if i>=3:
      return {'cnt': [6,8,8,8], 'Sum': curSum * 1.6}
    maxres=None
    for j in range(levels[i], maxLevels[i]+1):
      res=search(i+1, sigma, curSum)
      if maxres==None or res['Sum'] >= maxres['Sum']:
        maxres = res
        maxres['cnt'].append(j)

      sigma -= researchCost(j)
      if sigma < 0:break
      curSum +=vals[i]
    return maxres

  return search(0,sigma,curSum)