import pandas as pd

# 1. قراءة ملف الإكسل
try:
    df = pd.read_excel('data.xlsx')
    
    print("--- G-Systems Global: Smart Palm Analysis ---")

    for index, row in df.iterrows():
        # استخراج البيانات بناءً على أسماء الأعمدة الجديدة
        code = row['Sample_Code']
        palm_type = row['palm_type']
        elasticity = row['Modulus_of_Elasticity']
        location = row['Location']
        
        print(f"\n[+] Analyzing Sample: {code} ({palm_type})")
        print(f"    Origin: {location}")

        # خوارزمية فحص المرونة (بناءً على الكلمات الواردة في الإكسل)
        if elasticity == "عالي":
            print("    Result: Excellent for flexible packaging.")
        elif elasticity == "متوسط":
            print("    Result: Good for rigid boxes.")
        else:
            print("    Result: Low flexibility - recommended for composite wood.")

except Exception as e:
    print("Error: Please check the Excel file or Column names.")
    print(e)