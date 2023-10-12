###This project is to calculate certain mathematical solutions towards water resource management
###The approach is based around inputting data for calculations of water resource based problems such as precipitation, evaporation and runoff measurements
import math
def main():
    print("Index: ")
    print("R - Rainfall \nE - Evaporation \nRU - Runoff \n")
    print("Enter parameter of calculation: ")
    maininput = str(input())
    print()
    if (str(maininput) == "R") or (str(maininput) == "r"):
        print("You have selected Rainfall Calculations.")
        print("Rainfall Index: \nAM - Arithmatic Mean \nTP - Thiessen Polygon \nIS - Isohyetal Method")
        print()
        print("Enter method of Calculation: ")
        Rinput = str(input())
        print()
        if (str(Rinput) == "AM"):
            print("Arithmatic Mean Method")
            print("Enter number of stations: ")
            stations1 = int(input())
            sum1 = 0
            for i in range(stations1):
                print("Enter precipitation in mm: ")
                ppt1 = float(input())
                sum1 += ppt1
            AMppt = sum1/stations1
            print("Arithmatic mean precipitation is: ", AMppt)
        elif (str(Rinput) == "TP"):
            print("Thiessen Polygon Method")
            print("Enter number of stations: ")
            stations2 = int(input())
            sumppt1 = 0
            sumarea1 = 0
            for i in range (stations2):
                print("Enter area of station and precipitation: ")
                area1, ppt2 = input().split()
                sumppt1 += float(ppt2)*float(area1)
                sumarea1 += float(area1)
            TPppt = (sumppt1/sumarea1)
            print("Thiessen polygon precipitation in mm: ", TPppt)
        elif (str(Rinput) == "IS"):
            print("Isohyetal Method")
            print("Enter the number of isohyets: ")
            stations3 = int(input())
            sumppt2 = 0
            sumarea2 = 0
            for i in range(stations3):
                print("Enter isohyet and area between isohyets: ")
                isohyet, area2 = input().split()
                sumppt2 += float(isohyet)*float(area2)
                sumarea2 += float(area2)
            ISppt = sumppt2/sumarea2
            print("Isohyetal Precipitation: ", ISppt)
        else:
            print("Incorrect input.")
    elif (str(maininput) == "E") or (str(maininput) == "e"):
        print("You have selected Evaporation calculations.")
        print("Evaporation Index: \nBC - Blaney Criddle\nPW - Phi and W Index\nHE - Horton's Equation\nPM - Phillip's Method")
        print()
        print("Enter mode of calculation: ")
        Einput = str(input())
        print()
        if (str(Einput)=="BC"):
            print("Blaney-Criddle Method")
            print("Input p (Mean percent of annual daytime hours): ")
            p = float(input())
            print("Input Tmax in C: ")
            Tmax = float(input())
            print("Input Tmin in C: ")
            Tmin = float(input())
            Tmean = ((Tmax+Tmin)/2)
            EtoBC = p*((0.46*Tmean)+8)
            print("Evapotranspiration in mm/day: ", EtoBC)
        elif (str(Einput) == "PW"):
            print("Phi and W Index")
            print("Input total precipitation: ")
            P = float(input())
            print("Input total runoff: ")
            R = float(input())
            print("Input initial losses: ") #Enter 0 if calculating only phi index
            Ia = float(input())
            print("Input duration of study: ")
            tphi = int(input())
            phi = ((P-R)/tphi)
            Wind = ((P-R-Ia)/tphi)
            print("Phi index: ", phi)
            print("W index: ", Wind)
        elif (str(Einput) == "HE"):
            print("Horton's Equation")
            print("Input fc: ")
            fc = float(input())
            print("Input fo: ")
            fo = float(input())
            print("Input time: ")
            tHE = int(input())
            print("Input K: ")
            K = float(input())
            term1 = fc*tHE
            term2 = ((fo -fc)/K)
            term3 = (1-(math.exp(float(-K*tHE))))
            F = term1 + (term2*term3)
            print("F in in/h: ", F)
        elif (str(Einput) == "PM"):
            print("Phillip's Method")
            print("Input sorptivity of soil: ")
            sorp = float(input())
            print("Input time: ")
            PMtime = float(input())
            print("Input K: ")
            KPM = float(input())
            texp1 = math.pow(PMtime, 0.5)
            FPM = (sorp*texp1)+(KPM*PMtime)
            print("F: ", FPM, "cm")
            texp2 = math.pow(PMtime, -0.5)
            infil = (0.5*sorp*texp2)+KPM
            print("Infiltration rate: ", infil, "cm/h")
        else:
            print("Incorrect Input.")
    elif (str(maininput) == "RU"):
        print("You have selected Runoff calculations.")
        print("Runoff Index:\nIn - Interception\nRC - Runoff Coefficient\nRM - Rational Method")
        print()
        print("Enter mode of calculation: ")
        RUinput = str(input())
        print()
        if (str(RUinput) == "In"):
            print("Interception")
            print("Input Intercept Storage: ")
            Si = float(input())
            print("Input K: ")
            Ki = float(input())
            print("Input Et: ")
            Et = float(input())
            Int = Si + (Ki*Et)
            print("Interception: ", Int)
        elif (str(RUinput) == "RC"):
            print("Runoff Coefficient.")
            print("Input water yield: ")
            Yap = float(input())
            print("Input area of catchment: ")
            ARUC  = float(input())
            print("Input precipitation: ")
            RUppt = float(input())
            RUCoeff = (Yap/(ARUC*RUppt))
            print("Runoff Coefficient: ", RUCoeff)
        elif (str(RUinput) == "RM"):
            print("Rational Method.")
            print("Enter number of watershed areas: ")
            WSno = int(input())
            RMsumC = 0
            RMsumA = 0
            for i in range(WSno):
                print("Enter area of watershed and runoff coefficient: ")
                WSarea, WSRC = input().split()
                RMsumC += float(WSarea)*float(WSRC)
                RMsumA += float(WSarea)
            Cint = RMsumC/RMsumA
            print("Input Length: ")
            LRM = float(input())
            print("Input slope in percentage: ")
            SRM = float(input())
            LRMexp = math.pow(LRM, 0.77)
            SRMexp = math.pow((SRM/100), -0.385)
            TRM = 0.0195*LRMexp*SRMexp
            print("C: ", Cint)
            print("T: ", TRM, "min")
        else:
            print("Incorrect input.")
    else:
        print("Incorrect Input.")
    return 0

if __name__ == '__main__' :
    main()
