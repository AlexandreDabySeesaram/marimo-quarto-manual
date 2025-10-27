def gross2taxable_net(gross_salary):
    return 0.792893401*gross_salary

def gross2annual_net(gross_salary):
    return 12*0.792893401*gross_salary

def annual_taxable_net(gross_salary):
    return 12*gross2taxable_net(gross_salary)



def taxes(annual_taxable_net, threshold_1 = 11497.0, threshold_2 = 29315.0):
    # print(f"salary : {annual_taxable_net/12}")
    thirty_part = max((0.9*annual_taxable_net - threshold_2,0))
    thirty_tax = 0.3*thirty_part
    print(f"30 pourcents : {thirty_tax}")
    second_pal_tax = 0.11*(threshold_2-threshold_1)
    print(f"11 pourcents : {second_pal_tax}")
    return second_pal_tax+thirty_tax