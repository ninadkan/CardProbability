import itertools
from itertools import product
from enum import Enum
import numbers

# This module calculates the probability of getting alternate cards or sequence cards , when 3-6 cards are dealt 
class PairPairing(Enum):
    AlternatePairs = 1
    SequencePairs = 2
    NormalPair = 3   


lstColumnNames = [  'Pair Type',
                    'Number Of Cards Dealt', 
                    'Total Combinations',
                    'No Match',
                    'One Match',
                    'Two Match',
                    'Three Match',
                    'Trail Match',
                    'Double Trail Match',
                    'Four Of a Kind Match',
                    'Full House Match',
                    'Four of a Kind and a Pair Match',
                    'Total Matches',
                    'Probability - No Match ',
                    'Probability - One Match',
                    'Probability - Two Match',
                    'Probability - Three Match',
                    'Probability - Trail Match',
                    'Probability - Double Trail Match',
                    'Probability - Four Of a Kind Match',
                    'Probability - Full House Match',
                    'Probability - Four of a Kind and a Pair Match',
                    'Probability - Total Matches']
    
globalRowsToBeAdded = []

def writeExcel():
    import pandas as pd
    #import xlsxwriter
    df = pd.DataFrame(globalRowsToBeAdded, columns=lstColumnNames)
    outputFileName = 'probabilityOutput.xlsx'
    writer = pd.ExcelWriter(outputFileName, engine='xlsxwriter')
    df.to_excel(writer)
    writer.close()
    df = None
    


def addRowsToGlobalList(typeName,
                        nNumberOfCardsDealt, 
                        nTotalCount,
                        nZeroElementFound,
                        nOneElementFound,
                        nTwoElementFound =0,
                        nThreeElementFound=0,
                        nTripleElementFound=0,
                        nDoubleTripleElementFound=0, 
                        nFourOfAKindFound=0,
                        nFullHouseFound=0,
                        nFourOfAKindAndPair =0):
    global globalRowsToBeAdded
    totalelements = nOneElementFound+nTwoElementFound+nThreeElementFound+nTripleElementFound+nDoubleTripleElementFound+nFourOfAKindFound+nFullHouseFound+nFourOfAKindAndPair
    numberOfDecimalPlaces=6
    rowvalue = [typeName,
                nNumberOfCardsDealt, 
                nTotalCount,
                nZeroElementFound,
                nOneElementFound,
                nTwoElementFound,
                nThreeElementFound,
                nTripleElementFound,
                nDoubleTripleElementFound,
                nFourOfAKindFound,
                nFullHouseFound,
                nFourOfAKindAndPair ,
                totalelements, 
                round(nZeroElementFound/nTotalCount,numberOfDecimalPlaces),
                round(nOneElementFound/nTotalCount,numberOfDecimalPlaces),
                round(nTwoElementFound/nTotalCount,numberOfDecimalPlaces),
                round(nThreeElementFound/nTotalCount,numberOfDecimalPlaces),
                round(nTripleElementFound/nTotalCount,numberOfDecimalPlaces),
                round(nDoubleTripleElementFound/nTotalCount,numberOfDecimalPlaces),
                round(nFourOfAKindFound/nTotalCount,numberOfDecimalPlaces), 
                round(nFullHouseFound/nTotalCount,numberOfDecimalPlaces), 
                round(nFourOfAKindAndPair/nTotalCount,numberOfDecimalPlaces),
                round(totalelements/nTotalCount,numberOfDecimalPlaces)]
    globalRowsToBeAdded.append(rowvalue)
    return

        # # second iteration now
        # lstFirstColumnNames = [
        #             'combinationLength' ,
        #             'combinationValue' ,
        #             'CombinationIndex', 
        #             'FourOfAKindFound',
        #             'FourOfAKindIndexes',
        #             'FirstTripleFound',
        #             'FirstTripleIndexes',
        #             'SecondTripleFound',
        #             'SecondTripleIndexes'
        #             ]

        # dfFirstRegister = pd.DataFrame(completeList, columns=lstFirstColumnNames)
        # dfFirstRegister.set_index('CombinationIndex', inplace=True)
        # print(dfFirstRegister)        

        # lstColumnNames = [  'CardType',
        #                     'Number Of Cards Dealt', 
        #                     'Total Combinations',
        #                     'No-Match',
        #                     'One-Match',
        #                     'Two-Match',
        #                     'Three-Match',
        #                     'Trail-Match',
        #                     'Four-Of-A-Kind-Match',
        #                     'Full-House-Match',
        #                     'Four-of-A-Kind-N-A-Pair-Match']    
        
        # # creating a dataframe object
        # import pandas as pd
        # register = pd.DataFrame(columns=lstColumnNames)
        # register.set_index('Number Of Cards Dealt', inplace=True)

        
 
            # print("number of items in the list = {}".format(len(completeList)))
            # print(completeList[i])
            # insert a place-holder row. 

def findAllCalculationsForTwoCards(completeList, numberOfCardsDealt):
    numberOfElementsFound = 0
    for p in range(len(completeList)):
        for i in range(numberOfCardsDealt):
            for j in range (i+1, numberOfCardsDealt):
                if (completeList[p]['combinationValue'][i] == completeList[p]['combinationValue'][j]):
                    numberOfElementsFound += 1
    #update the records
    zeroFound = (len(completeList) - numberOfElementsFound)
    addRowsToGlobalList(typeName=PairPairing.NormalPair.name, 
                        nNumberOfCardsDealt=numberOfCardsDealt,
                        nTotalCount=len(completeList), 
                        nZeroElementFound=zeroFound, 
                        nOneElementFound=numberOfElementsFound)    
    return

def findAllCalculationsForThreeCards(completeList, numberOfCardsDealt):
    numberOfElementsFound = 0
    numberOfTripleFound = 0
    for p in range(len(completeList)):
        if (completeList[p]['FirstTripleFound'] == True) :
            numberOfTripleFound += 1
        else:
            for i in range(numberOfCardsDealt):
                for j in range (i+1, numberOfCardsDealt):
                    if (completeList[p]['combinationValue'][i] == completeList[p]['combinationValue'][j]):
                        numberOfElementsFound += 1
                        break
    #update the records
    zeroFound = (len(completeList) - (numberOfElementsFound + numberOfTripleFound))
    addRowsToGlobalList(typeName=PairPairing.NormalPair.name, 
                        nNumberOfCardsDealt=numberOfCardsDealt,
                        nTotalCount=len(completeList), 
                        nZeroElementFound=zeroFound, 
                        nOneElementFound=numberOfElementsFound,
                        nTripleElementFound=numberOfTripleFound)        
    return

def findAllCalculationsForFourCards(completeList, numberOfCardsDealt):
    numberOfElementsFound = 0
    numberOfTripleFound = 0
    numberOfDoublePairsFound =0
    numberOfFourOfAKindFound =0
    for p in range(len(completeList)):
        if (completeList[p]['FourOfAKindFound'] == True) :
            numberOfFourOfAKindFound += 1
        else:
            if (completeList[p]['FirstTripleFound'] == True) :
                numberOfTripleFound += 1 
            else:
                alreadyFoundIndex = [] 
                for i in range(numberOfCardsDealt):
                    if i not in alreadyFoundIndex:
                        for j in range (i+1, numberOfCardsDealt):
                            if j not in alreadyFoundIndex:
                                if (completeList[p]['combinationValue'][i] == completeList[p]['combinationValue'][j]):
                                    numberOfElementsFound += 1
                                    alreadyFoundIndex.append(i)
                                    alreadyFoundIndex.append(j)
                if (len(alreadyFoundIndex) == 4):
                    numberOfElementsFound -= 2
                    numberOfDoublePairsFound += 1
    #update the records
    zeroFound = (len(completeList) - (numberOfElementsFound + numberOfTripleFound + numberOfDoublePairsFound+numberOfFourOfAKindFound))
    addRowsToGlobalList(typeName=PairPairing.NormalPair.name, 
                        nNumberOfCardsDealt=numberOfCardsDealt,
                        nTotalCount=len(completeList), 
                        nZeroElementFound=zeroFound, 
                        nOneElementFound=numberOfElementsFound,
                        nTripleElementFound=numberOfTripleFound,
                        nTwoElementFound=numberOfDoublePairsFound,
                        nFourOfAKindFound=numberOfFourOfAKindFound)        
    return

def findAllCalculationsForFiveCards(completeList, numberOfCardsDealt):
    numberOfElementsFound = 0
    numberOfTripleFound = 0
    numberOfDoublePairsFound =0
    numberOfFourOfAKindFound =0
    numberOfFullHouseFound = 0
    for p in range(len(completeList)):
        if (completeList[p]['FourOfAKindFound'] == True) :
            numberOfFourOfAKindFound += 1
        else:
            if (completeList[p]['FirstTripleFound'] == True) :
                numberOfTripleFound += 1
                # lets get a list of all indexes
                lstAllIndexes = list(range(numberOfCardsDealt))
                # now subtract this list with the one in master list
                c = [x for x in lstAllIndexes if x not in completeList[p]['FirstTripleIndexes']]
                if (completeList[p]['combinationValue'][c[0]] == completeList[p]['combinationValue'][c[1]]):
                    numberOfFullHouseFound += 1
                    numberOfTripleFound -= 1
            else:
                alreadyFoundIndex = [] 
                for i in range(numberOfCardsDealt):
                    if i not in alreadyFoundIndex:
                        for j in range (i+1, numberOfCardsDealt):
                            if j not in alreadyFoundIndex:
                                if (completeList[p]['combinationValue'][i] == completeList[p]['combinationValue'][j]):
                                    numberOfElementsFound += 1
                                    alreadyFoundIndex.append(i)
                                    alreadyFoundIndex.append(j)
                if (len(alreadyFoundIndex) == 4):
                    numberOfElementsFound -= 2
                    numberOfDoublePairsFound += 1
    #update the records
    zeroFound = (len(completeList) - (numberOfElementsFound + numberOfTripleFound + numberOfDoublePairsFound + numberOfFourOfAKindFound + numberOfFullHouseFound))
    addRowsToGlobalList(typeName=PairPairing.NormalPair.name, 
                        nNumberOfCardsDealt=numberOfCardsDealt,
                        nTotalCount=len(completeList), 
                        nZeroElementFound=zeroFound, 
                        nOneElementFound=numberOfElementsFound,
                        nTripleElementFound=numberOfTripleFound,
                        nTwoElementFound=numberOfDoublePairsFound,
                        nFourOfAKindFound=numberOfFourOfAKindFound,
                        nFullHouseFound=numberOfFullHouseFound)                   
    
    return 

def findAllCalculationsForSixCards(completeList, numberOfCardsDealt):

    numberOfSinglePairFound = 0
    numberOfDoublePairsFound =0
    numberOfThreePairsFound =0
    numberOfTripleFound = 0
    numberOfFourOfAKindFound =0
    numberOfDoubleTripleElementFound =0
    numberOfFourOfAKindAndPairFound=0
    numberOfFullHouseFound =0
    

    for p in range(len(completeList)):
        if (completeList[p]['FourOfAKindFound'] == True) :
            numberOfFourOfAKindFound += 1
            # lets get a list of all indexes
            lstAllIndexes = list(range(numberOfCardsDealt))
            # now subtract this list with the one in master list
            c = [x for x in lstAllIndexes if x not in completeList[p]['FourOfAKindIndexes']]
            if (completeList[p]['combinationValue'][c[0]] == completeList[p]['combinationValue'][c[1]]):
                numberOfFourOfAKindAndPairFound += 1
                numberOfFourOfAKindFound -= 1 
        else:
            if (completeList[p]['SecondTripleFound'] == True) :
                numberOfDoubleTripleElementFound += 1
            else: 
                if (completeList[p]['FirstTripleFound'] == True) :
                    numberOfTripleFound += 1
                    # lets get a list of all indexes
                    lstAllIndexes = list(range(numberOfCardsDealt))
                    # now subtract this list with the one in master list
                    co = [x for x in lstAllIndexes if x not in completeList[p]['FirstTripleIndexes']]
                    #print(co)
                    alreadyFound= []
                    for l in range(len(co)):
                        if l not in alreadyFound:
                            for m in range (l+1, len(co)):
                                if m not in alreadyFound:
                                    if (completeList[p]['combinationValue'][co[l]] == completeList[p]['combinationValue'][co[m]]):
                                        numberOfFullHouseFound += 1
                                        numberOfTripleFound -= 1
                                        alreadyFound.append(l)
                                        alreadyFound.append(m)
                else:
                    alreadyFoundIndex = [] 
                    for i in range(numberOfCardsDealt):
                        if i not in alreadyFoundIndex:
                            for j in range (i+1, numberOfCardsDealt):
                                if j not in alreadyFoundIndex:
                                    if (completeList[p]['combinationValue'][i] == completeList[p]['combinationValue'][j]):
                                        numberOfSinglePairFound += 1
                                        alreadyFoundIndex.append(i)
                                        alreadyFoundIndex.append(j)
                    if (len(alreadyFoundIndex) == 6):
                        numberOfSinglePairFound -= 3
                        numberOfThreePairsFound += 1
                    else :
                        if (len(alreadyFoundIndex) == 4):
                            numberOfSinglePairFound -= 2
                            numberOfDoublePairsFound += 1
    #update the records
    zeroFound = (len(completeList) - (numberOfSinglePairFound + numberOfTripleFound + 
                                        numberOfDoublePairsFound + numberOfFourOfAKindFound + 
                                        numberOfDoubleTripleElementFound + numberOfFourOfAKindAndPairFound +
                                        numberOfFullHouseFound + numberOfThreePairsFound))
    addRowsToGlobalList(typeName=PairPairing.NormalPair.name, 
                        nNumberOfCardsDealt=numberOfCardsDealt,
                        nTotalCount=len(completeList), 
                        nZeroElementFound=zeroFound, 
                        nOneElementFound=numberOfSinglePairFound,
                        nTripleElementFound=numberOfTripleFound,
                        nTwoElementFound=numberOfDoublePairsFound,
                        nThreeElementFound=numberOfThreePairsFound,
                        nFourOfAKindFound=numberOfFourOfAKindFound,
                        nFullHouseFound=numberOfFullHouseFound,
                        nDoubleTripleElementFound=numberOfDoubleTripleElementFound,
                        nFourOfAKindAndPair=numberOfFourOfAKindAndPairFound) 
    return
    
def CalculateProbabilityGettingPairs(numberOfCardsDealt) :
    # print(PairPairingTypeValue)

    # if not isinstance(PairPairingTypeValue, PairPairing):
    #     raise TypeError('PairPairingTypeValue must be an instance of PairPairing Enum')
    # valid inputs. should be between 3 and 6
    if (numberOfCardsDealt >= 2 ) and (numberOfCardsDealt <= 6) : 
        v = list(range(1, 14)) * 4
        v.sort()
        # print (v)
        # [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
        #v= list(range(0,52))

       
 
        completeList = []
        rowDict = { 'combinationLength' : -1,
                    'combinationValue' : [],
                    'CombinationIndex' : -1, 
                    'FourOfAKindFound': False,
                    'FourOfAKindIndexes' : [],
                    'FirstTripleFound': False,
                    'FirstTripleIndexes': [],
                    'SecondTripleFound': False,
                    'SecondTripleIndexes': []
                    }
        nCount =0

        for c in itertools.combinations(v, numberOfCardsDealt): # iterate through all the combinations
            rowDict['combinationLength'] = len(c)
            rowDict['CombinationIndex'] = nCount
            rowDict['combinationValue'] = list(c)
            nCount += 1
            alreadySelectedIndex = []
            for i in range (len(c)):
                bTripleFound = False
                bFourOfAKindFound = False
                bSecondTripleFound = False
                if i not in alreadySelectedIndex: 
                    for j in range (i+1, len(c)):
                        if j not in alreadySelectedIndex:
                            if (numberOfCardsDealt > 3): #4,5,6; First find four of a kind
                                for k in range (j+1, len(c)):
                                    if (k not in alreadySelectedIndex) and (bFourOfAKindFound == False): 
                                        for l in range (k+1, len(c)):
                                            if not l in alreadySelectedIndex and (bFourOfAKindFound == False):
                                                if (c[i] == c[j] == c[k] == c[l]):
                                                    alreadySelectedIndex.append(i)
                                                    alreadySelectedIndex.append(j)
                                                    alreadySelectedIndex.append(k)
                                                    alreadySelectedIndex.append(l)
                                                    bFourOfAKindFound = True
                                                    rowDict['FourOfAKindFound'] = True
                                                    rowDict['FourOfAKindIndexes'] = [i,j,k,l]
                                                    break;
                            if (bFourOfAKindFound == False) :
                                if (numberOfCardsDealt > 2): # 3,4,5,6
                                    for k in range (j+1, len(c)):
                                        if (k not in alreadySelectedIndex) and (bTripleFound == False) : 
                                            if (c[i] == c[j] == c[k]):
                                                alreadySelectedIndex.append(i)
                                                alreadySelectedIndex.append(j)                                                        
                                                alreadySelectedIndex.append(k)
                                                bTripleFound = True
                                                rowDict['FirstTripleFound'] = True
                                                rowDict['FirstTripleIndexes'] = [i,j,k]
                                                break
                            # special case of double triples : AAABBB
                            if ((bFourOfAKindFound == False) and (bTripleFound ==True) and (numberOfCardsDealt ==6)):
                                for p in range (len(c)):
                                    if p not in alreadySelectedIndex:
                                        for q in range (p+1, len(c)):
                                            if q not in alreadySelectedIndex:
                                                for r in range (q+1, len(c)):
                                                    if  (c[p] == c[q] == c[r]):
                                                        # nTripleElementFound += 1 # otherwise it'll be double counted. 
                                                        alreadySelectedIndex.append(p)
                                                        alreadySelectedIndex.append(q)                                                        
                                                        alreadySelectedIndex.append(r)
                                                        bSecondTripleFound = True 
                                                        rowDict['SecondTripleFound'] = True
                                                        rowDict['SecondTripleIndexes'] = [p,q,r]                                                            
                                                        break

 
            completeList.append(rowDict.copy()) # needed to copy, else everything was just empty
            
            # reset the dictionary object
            rowDict['combinationLength'] = -1
            rowDict['combinationValue'] = []
            rowDict['CombinationIndex'] = -1
            rowDict['FourOfAKindFound']= False
            rowDict['FourOfAKindIndexes'] = []
            rowDict['FirstTripleFound']= False
            rowDict['FirstTripleIndexes']= []
            rowDict['SecondTripleFound']= False
            rowDict['SecondTripleIndexes']= []

        # second iteration to calculate the remaining pairs 
        match numberOfCardsDealt:
            case 2:
                findAllCalculationsForTwoCards(completeList, numberOfCardsDealt)
            case 3:
                findAllCalculationsForThreeCards(completeList, numberOfCardsDealt)
            case 4:
                findAllCalculationsForFourCards(completeList, numberOfCardsDealt)
            case 5:
                findAllCalculationsForFiveCards(completeList, numberOfCardsDealt)
            case 6:
                findAllCalculationsForSixCards(completeList, numberOfCardsDealt)             
            case _:
                pass
                    
            # if (completeList[i]['FourOfAKindFound'] == True) :
            #     print("FourOfAKind {}, {}, {}, {}".format(completeList[i]['combinationLength'],completeList[i]['combinationValue'], completeList[i]['CombinationIndex'], completeList[i]['FourOfAKindIndexes'] ))
            # if (completeList[i]['FirstTripleFound'] == True) :
            #     print("First Triple {}, {}, {}, {}".format(completeList[i]['combinationLength'],completeList[i]['combinationValue'], completeList[i]['CombinationIndex'], completeList[i]['FirstTripleIndexes'] ))
            # if (completeList[i]['SecondTripleFound'] == True) :
            #     print("Second Triple {}, {}, {}. {}".format(completeList[i]['combinationLength'],completeList[i]['combinationValue'], completeList[i]['CombinationIndex'], completeList[i]['SecondTripleIndexes'] ))                
    else:
        raise TypeError('numberOfCardsDealt parameter needs to be between 2 and 6 (inclusive)')
    return
    
# this function calculates either alternate Element or sequence calculations
def calculateProbability(numberOfCardsDealt, PairPairingTypeValue, debug=False) :
    if not isinstance(PairPairingTypeValue, PairPairing):
        raise TypeError('PairPairingTypeValue must be an instance of PairPairing Enum')
    nCount = 0
    nZeroElementFound =0
    nnOneElementFound = 0
    nnTwoElementFound =0
    nThreeElementFound = 0


    # valid inputs. should be between 3 and 6
    if (numberOfCardsDealt >= 2 ) and (numberOfCardsDealt <= 6) : 
        v = list(range(1, 14)) * 4
        v.sort()

        for c in itertools.combinations(v, numberOfCardsDealt):
            nCount += 1
            numberOfElementFound =0
            alreadySelectedIndex = []
            for i in range (len(c)):
                 if i not in alreadySelectedIndex: 
                    for j in range (i+1, len(c)):
                        if j not in alreadySelectedIndex:
                            boolConditionSatisfied = False
                            match PairPairingTypeValue.value: # this match case will be triggered in every loop, is this effecient? 
                                case PairPairing.AlternatePairs.value:
                                # special case of Ace - Queen pairing. 
                                    if (((c[i] == 1) and (c[j] == 12)) or ((c[i] == 12) and (c[j] == 1))):
                                        boolConditionSatisfied = True
                                    else:
                                        # alternate match is current +- 2. 
                                        if  ((c[i] == (c[j] - 2) ) or (c[i] == (c[j] + 2))):
                                            boolConditionSatisfied = True 
                                case PairPairing.SequencePairs.value:
                                    # special case of Ace - King pairing. 
                                    if (((c[i] == 1) and (c[j] == 13)) or ((c[i] == 13) and (c[j] == 1))):
                                        boolConditionSatisfied = True
                                    else:
                                        # alternate match is current +- 1. 
                                        if  ((c[i] == (c[j] - 1) ) or (c[i] == (c[j] + 1))):
                                            boolConditionSatisfied = True 
                            if (boolConditionSatisfied == True):
                                numberOfElementFound += 1
                                alreadySelectedIndex.append(i)
                                alreadySelectedIndex.append(j)                                
                                break
            match numberOfElementFound:
                case 0:
                    nZeroElementFound += 1
                case 1:
                    nnOneElementFound += 1
                case 2:
                    nnTwoElementFound += 1
                case 3:
                    nThreeElementFound += 1
                case _:
                    print("Error - default triggered!!! {}".format(c))
                    nZeroElementFound += 1
                    raise ValueError('Error - default triggered!!!')
            if (debug):
                if (numberOfElementFound > 0):
                    print ("Total Element Found = {}, values = {}".format(numberOfElementFound, c))
                
    return numberOfCardsDealt, nCount, nZeroElementFound, nnOneElementFound, nnTwoElementFound, nThreeElementFound,0,0,0,0


def probabilityGettingAStraight(numberOfCardsDealt=5,debug=False) :
    # (45678); sequence impure
    return

def probabilityGettingAFlush(numberOfCardsDealt=2,debug=False) :
    # Cards of Same colour
    return

def probabilityGettingAStraightFlush(numberOfCardsDealt=2,debug=False) :
    # Cards of Same colour and a pure sequence
    return

def probabilityGettingARoyalFlush(numberOfCardsDealt=2,debug=False) :
    # Cards of Same colour and a pure sequence
    return

# enumList = list(PairPairing)

# lstColumnNames = [  'Pair Type',
#                     'Number Of Cards Dealt', 
#                     'Total Combinations',
#                     'No Match',
#                     'One Match',
#                     'Two Match',
#                     'Three Match',
#                     'Trail Match',
#                     'Four Of a Kind Match',
#                     'Full House Match',
#                     'Four of a Kind and a Pair Match',
#                     'Total Matches',
#                     'Probability - No Match ',
#                     'Probability - One Match',
#                     'Probability - Two Match',
#                     'Probability - Three Match',
#                     'Probability - Trail Match',
#                     'Probability - Four Of a Kind Match',
#                     'Probability - Full House Match',
#                     'Probability - Four of a Kind and a Pair Match',
#                     'Probability - Total Matches']

# rowsToBeAdded = []

# for enumValue in enumList:
#     for l in range(2,7):
#         numberOfCardsDealt, count, no_zeroElementFound, nOneElementFound, nTwoElementFound, ThreeElementFound, TripleElementFound, FourOfAKindFound ,FullHouseFound , FourOfAKindAndPair= calculateProbability(l, enumValue)
#         TotalCombined= no_zeroElementFound+nOneElementFound+nTwoElementFound+ThreeElementFound + TripleElementFound+ FourOfAKindFound +FullHouseFound + FourOfAKindAndPair
#         TotalElements = nOneElementFound+nTwoElementFound+ThreeElementFound +  TripleElementFound+ FourOfAKindFound +FullHouseFound + FourOfAKindAndPair
#         #print ("Card dealt = {}, Total combinaions = {}, Total Combined = {}, Total Elements = {}".format(numberOfCardsDealt, count,TotalCombined, TotalElements ))
#         # print(" Cards Dealt = {}; Element Sequence = {} ; Total combinations = {} ; Element Probabilities : Zero = {}, one = {}, two = {}, three = {} , Triple = {}, Four of a Kind = {}, Full House = {}, Four and Pair = {}".format( \
#         #                                                                                                                                                       numberOfCardsDealt,
#         #                                                                                                                                                       enumValue.name, 
#         #                                                                                                                                                       count, 
#         #                                                                                                                                                       round(no_zeroElementFound/count,3),
#         #                                                                                                                                                       round(nOneElementFound/count,3), 
#         #                                                                                                                                                       round(nTwoElementFound/count,3), 
#         #                                                                                                                                                       round(ThreeElementFound/count,3),
#         #                                                                                                                                                       round(TripleElementFound/count,3),
#         #                                                                                                                                                       round(FourOfAKindFound/count,3), 
#         #                                                                                                                                                       round(FullHouseFound/count,3), 
#         #                                                                                                                                                       round(FourOfAKindAndPair/count,3)))
#         # print("     Zero Elements = {}, One Elements = {}, Two Elements = {}, Three Elements = {}, Total = {}, Triple = {}, Four of a Kind = {}, Full House = {}, Four and Pair = {}".format(
#         #                                                                                                                 no_zeroElementFound,
#         #                                                                                                                 nOneElementFound, 
#         #                                                                                                                 nTwoElementFound, 
#         #                                                                                                                 ThreeElementFound,
#         #                                                                                                                 TotalElements,
#         #                                                                                                                 TripleElementFound,
#         #                                                                                                                 FourOfAKindFound,
#         #                                                                                                                 FullHouseFound,
#         #                                                                                                                 FourOfAKindAndPair))

 
#         # Some data we want to write to the worksheet.
#         RowValue = [enumValue.name,
#                     numberOfCardsDealt, 
#                     count,
#                     no_zeroElementFound,
#                     nOneElementFound,
#                     nTwoElementFound,
#                     ThreeElementFound,
#                     TripleElementFound,
#                     FourOfAKindFound,
#                     FullHouseFound,
#                     FourOfAKindAndPair ,
#                     TotalElements, 
#                     round(no_zeroElementFound/count,3),
#                     round(nOneElementFound/count,3),
#                     round(nTwoElementFound/count,3),
#                     round(ThreeElementFound/count,3),
#                     round(TripleElementFound/count,3),
#                     round(FourOfAKindFound/count,3), 
#                     round(FullHouseFound/count,3), 
#                     round(FourOfAKindAndPair/count,3),
#                     round(TotalElements/count,3)]
#         rowsToBeAdded.append(RowValue)
#         #print(len(RowValue))



# import pandas as pd

# #import xlsxwriter
# df = pd.DataFrame(rowsToBeAdded, columns=lstColumnNames)
# # print("--------------------------------------------------")
# # print(df)
# # print(enumValue.name)
# # print("--------------------------------------------------")
# outputFileName = 'probabilityOutput.xlsx'
# writer = pd.ExcelWriter(outputFileName, engine='xlsxwriter')
# df.to_excel(writer)
# writer.close()
# df = None


enumList = list(PairPairing)
for enumValue in enumList:
    for l in range(2,7): 
        print(l)
        numberOfCardsDealt, count, nZeroElementFound, \
        numberOfSinglePairFound, numberOfDoublePairsFound, numberOfThreePairsFound, \
        numberOfTripleFound, numberOfFourOfAKindFound ,numberOfFullHouseFound , \
        numberOfFourOfAKindAndPairFound= calculateProbability(l, enumValue)
        addRowsToGlobalList(typeName=PairPairing.NormalPair.name, 
                            nNumberOfCardsDealt=numberOfCardsDealt,
                            nTotalCount=count, 
                            nZeroElementFound=nZeroElementFound, 
                            nOneElementFound=numberOfSinglePairFound,
                            nTripleElementFound=numberOfTripleFound,
                            nTwoElementFound=numberOfDoublePairsFound,
                            nThreeElementFound=numberOfThreePairsFound,
                            nFourOfAKindFound=numberOfFourOfAKindFound,
                            nFullHouseFound=numberOfFullHouseFound,
                            nDoubleTripleElementFound=0,
                            nFourOfAKindAndPair=numberOfFourOfAKindAndPairFound) 
        CalculateProbabilityGettingPairs(l)


writeExcel()
