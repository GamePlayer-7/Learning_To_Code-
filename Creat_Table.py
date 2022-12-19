table = [['Name', 'Location', 'Age'], 
         ['Ram', 'Mumbai', 27], 
         ['Sham', 'Nagpur, 25], 
         ['Laxman', 'Pune', 28]]

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
