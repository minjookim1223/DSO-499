# Lab 10: Emergency department triage of acute cardiac ischemia
# Minjoo Kim (Jay)
# minjook@usc.edu

# prompts
welcome_msg = 'Welcome to the Emergency Department Decision Support System'
q1 = 'Q1: Is there ECG evidence of acute Myocardial Infarction (MI)? (Y/N) '
q2 = 'Q2: Is there ECG evidence of acute Ischemia? (Y/N) '
q3 = 'Q3: How many urgent factors are present? (0/1/2/3) '

### INSERT YOUR CODE BELOW THIS LINE ###


def main():
    inputOkay = False
    print(welcome_msg)

    while not inputOkay:
        myocardial = input(q1)
        if myocardial == 'Y':
            inputOkay = True
            break
        elif myocardial == 'N':
            ischemia = input(q2)
            if ischemia == 'Y' or ischemia == 'N':
                factors = input(q3)
                if factors.isdigit() and 0 <= int(factors) <= 3:
                    inputOkay = True
                else:
                    print("Invalid input. Please start over.")
                    break
            else:
                print("Invalid input. Please start over.")
                break
        else:
            print("Invalid input. Please start over.")
            break

    if inputOkay:
        if myocardial == "Y":
            assessment = "High Risk"
            assignment = "Coronary Care Unit"
        else:
            if ischemia == "Y":
                if 2 <= int(factors) <= 3:
                    assessment = "High Risk"
                    assignment = "Coronary Care Unit"
                else:
                    assessment = "Moderate Risk"
                    assignment = "Inpatient Telemetry Unit"
            else:
                if 2 <= int(factors) <= 3:
                    assessment = "Moderate Risk"
                    assignment = "Inpatient Telemetry Unit"
                elif int(factors) == 1:
                    assessment = "Low Risk"
                    assignment = "Inpatient Telemetry Unit"
                else:
                    assessment = "Very Low Risk"
                    assignment = "Observation Unit"

        print("Assessment:", assessment)
        print("Assignment:", assignment)


main()