import quadratic_polynomial as qp

# Identify if the equation has real solution or complex solution 
answer_quest = "yes"
while(answer_quest == "yes"):

    a, b, c = input("Please type the coefficients of the quadratic equation:").split()
    a = float(a)
    b = float(b)
    c = float(c)
    poly = qp.quadratic_polynomial(a, b, c)
    poly.general_formula()
    h,k=poly.vertex_formula()
    poly.plot_function()
    print("The vertex of this quadratic polynomial is {0:.5}, {1:.5} \n".format(h,k))
    answer_quest = input("\nDo you want to keep using the application? ")