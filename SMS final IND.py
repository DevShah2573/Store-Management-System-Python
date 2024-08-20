#########################################################################################
#                              STORE MANAGEMENT SYSTEM                                  #
################################################################--By Dev Shah--##########


import matplotlib.pyplot as plt
#########################################################################################
#                                    The Main Function                                  #
#########################################################################################

def main_interface():
    while(True):
        print()
        print("Select the Operation:")
        print("1. Add Customer               6. Add new product            11.Exit")
        print("2. All Customers Details      7. Add Product stock")
        print("3. Check Customers Details    8. Product sell")  
        print("4. All Product Details        9. Product Data chart")
        print("5. Check Product Details      10. Generate bill")
        print()
        select = input("Select :")
        if select == "1":
            add_new_customer()
        elif select == "2":
            all_customers_details()
        elif select == "3":
            check_customers_details()
        elif select == "4":
            All_product_details()
        elif select == "5":
            check_products_details()
        elif select == "6":
            add_new_product()
        elif select == "7":
            add_product_stock()
        elif select == "8":
            product_sold()
        elif select == "9":
            product_data_chart()
        elif select == "10":
            generate_bill()
        elif select == "11":
            break
        else:
            print("Please, Select Valid Option.")




#########################################################################################
#                              Some Important Functions                                 #
#########################################################################################

# This function, converts the multiline text file in to 2D list
def textdata_to_list2d(filename,stripstring="|"):
    f = open(filename,'r')
    f.seek(0)
    lst = f.read().split("\n")
    # print(lst)
    for i in range(len(lst)):
        lst[i] = lst[i].split(stripstring)
    # print(lst)
    f.close()
    return lst # now file is converted into the 2D List

# This function, converts the 2D list in to multiline text file
def list2d_to_textdata(lst,stripstring="|"):
    l1 = len(lst)
    for i in range(l1):
        l2 = len(lst[i])
        data=""
        for j in range(l2):
            data = data + stripstring +lst[i][j]
            data = data.strip(stripstring)
        lst[i] = data+"\n"
    text_data = "".join(lst)
    return text_data # now 2D list is converted into file

#########################################################################################
#                                      Functions                                        #
#########################################################################################

# 01
def add_new_customer():
    c_id = input("Enter Customer ID :")
    c_name = input("Enter Customer Name :")
    c_phone_no = input("Enter Customer Phone No. :")
    c_email = input("Enter Customer E-mail :")
    c_details = input("Enter Customer Details :")

    # Check Customer is already Exist or Not 
    customer_list = textdata_to_list2d("customers.txt")
    for c in customer_list:
        if(c[0]==c_id):
            print("Customer Already Exist with this ID. !!") 
            break
    else:
        customer = f"{c_id}|{c_name}|{c_phone_no}|{c_email}|{c_details}"+"\n"
        f = open("customers.txt","a")
        f.write(customer)
        f.close()

#----------------------------------------------------------------------------------------

# 02
def all_customers_details():
    f = open("customers.txt","r")
    print(f.read())
    f.close()

#----------------------------------------------------------------------------------------

# 03
def check_customers_details():
    cid = input("Enter the Customer ID:")
    customer_list = textdata_to_list2d("customers.txt")
    for c in customer_list:
        if c[0]== cid:
            print("Customer Details")
            print("ID           :",c[0])
            print("Name         :",c[1])
            print("Phone No.    :",c[2])
            print("E-mail       :",c[3])
            print("Description  :",c[4])
            break
    else:
        print("Customer(CID) Not Found !!")

#----------------------------------------------------------------------------------------
# 04
def All_product_details():
    f = open("products.txt","r")
    print(f.read())
    f.close()

#----------------------------------------------------------------------------------------

# 05
def check_products_details():
    pid = input("Enter the Product ID:")
    product_list = textdata_to_list2d("products.txt")
    for p in product_list:
        if p[0]==pid:
            print("Product Details")
            print("ID           :",p[0])
            print("Name         :",p[1])
            print("Price        :",p[2])
            print("Description  :",p[3])
            print("Sold(S)      :",p[4])
            print("Available(A) :",p[5])
            print("Total(S+A)   :",p[6])
            break
    else:
        print("Produnct(PID) Not Found !!")

#----------------------------------------------------------------------------------------

# 06
def add_new_product():
    p_id = input("Enter Product ID :")
    p_name = input("Enter Product Name :")
    p_price = input("Enter Product Price :")
    p_quantity = input("Enter Product Quantity :")
    p_details = input("Enter Product Details :")

    p_sold = 0
    p_available = p_quantity
    
    # Check Product is already Exist or Not 
    product_list = textdata_to_list2d("products.txt")
    for p in product_list:
        if(p[0]==p_id):
            print("Product Already Exist with this ID. !!") 
            break
    else:
        product = f"{p_id}|{p_name}|{p_price}|{p_details}|{p_sold}|{p_available}|{p_quantity}"+"\n"
        f = open("products.txt","a")
        f.write(product)
        f.close()

#----------------------------------------------------------------------------------------

# 07
def add_product_stock():
    flag=0
    pid = input("Enter Product ID :")
    add_quantity = int(input("Enter Quantity :"))
    product_list = textdata_to_list2d("products.txt")
    for p in product_list:
        if p[0]==pid:
            p[-1] = str(int(p[-1]) + add_quantity)
            p[-2] = str(int(p[-2]) + add_quantity)
            break
    else:
        print("Product ID Not found. !!")
        flag = 1
    if(flag!=1):
        f = open("products.txt","w")
        f.write(list2d_to_textdata(product_list).strip())
        f.close()

#----------------------------------------------------------------------------------------

# 08
def product_sold():
    flag=0
    pid = input("Enter Product ID :")
    sold_quantity = int(input("Enter Sold Quantity:"))
    product_list = textdata_to_list2d("products.txt")
    for p in product_list:
        if p[0]==pid:
            if int(p[-2]) - sold_quantity < 0:
                print(f"{sold_quantity} Quantity of {p[1]} is Not available !! ({p[-2]} Available)")
                break
            else:
                p[-2] = str(int(p[-2]) - sold_quantity)
                p[-3] = str(int(p[-3]) + sold_quantity)
                break
    else:
        print("Product ID Not found. !!")
        flag = 1
    if(flag!=1):
        f = open("products.txt","w")
        f.write(list2d_to_textdata(product_list).strip())
        f.close()

#----------------------------------------------------------------------------------------

# 09
def product_data_chart():
    plt.figure(figsize=(20,10))
    product_list = textdata_to_list2d("products.txt")

    p_names = [i[1] for i in product_list]
    p_sold = [int(i[-3]) for i in product_list]
    p_avilabel = [int(i[-2]) for i in product_list]

    plt.bar(p_names,p_sold,width=0.5,)
    plt.show()

    plt.pie(p_sold,labels=p_names,autopct="%1.1f%%")
    plt.title("Product Sell")
    plt.show()

#----------------------------------------------------------------------------------------

# 10
def generate_bill():
    print("==============================================")
    print("           DEV SHAH GENERAL STORE             ")
    print("==============================================")
    product_list = textdata_to_list2d("products.txt")
    
    grand_total = 0
    
    print(f"P.ID\tP.NAME\t\tPRICE\tQNTY\tTOTAL")
    print("----------------------------------------------")
    while(True):
        pid = input("Enter Product ID:")
        buy_quntity = int(input("How many quntity Buy? :"))
        for p in product_list:
            if p[0] == pid:
                if int(p[-2]) - buy_quntity < 0:
                    print(f"{buy_quntity} Quantity of {p[1]} is Not available !!({p[-2]} Available)")
                    break
                else:
                    grand_total += int(p[2])*buy_quntity
                    print(f"{p[0]}\t{p[1]}\t{int(p[2])}\t{buy_quntity}\t{int(p[2])*buy_quntity}")
                    
                    #Update file Data
                    p[-2] = str(int(p[-2]) - buy_quntity)
                    p[-3] = str(int(p[-3]) + buy_quntity)
                    break
        else:
            print(f"{pid}\tis not Available !!")
        want_to_add = input("Do you want to add Another item (y/n):").lower()
        if want_to_add=="n" or want_to_add=="no":
            break
    f = open("products.txt","w")
    f.write(list2d_to_textdata(product_list).strip())
    f.close()
    print("----------------------------------------------")
    print(f"YOUR GRAND TOTAL:{grand_total}")
    print("==============================================")
    print("         Thank You !! Visit Again !!          ")

# SOME REFERENCES
#   For products file
#   ID           : p[0])
#   Name         : p[1]
#   Price        : p[2]
#   Description  : p[3]
#   Sold(S)      : p[4] or p[-3]
#   Available(A) : p[5] or p[-2]
#   Total(S+A)   : p[6] or p[-1]
#########################################################################################
#                                       THE END                                         #
#                                  CREATED BY DEV SHAH                                  #
#########################################################################################

main_interface()