file_name = "application_data.csv"
file = open(file_name)

data = file.readlines()
print(data.pop(0))

for line in data:

    cols = line.split(',')

    (customerID,
    loanID,
    applicationDate,
    LoanNumber,
    LoanAmount,
    InterestRate,
    TermDays,
    RepaymentDueDAte,
    RepaymentPayDate) = (cols[0],
                        cols[1],
                        cols[2].replace('\n', '')
                        cols[3],
                        cols[4],
                        cols[5],
                        cols[6],
                        cols[7].replace
                        cols[8].replace('\n', ''))


    homework.add_datapoint(customerID,
                                loan)
