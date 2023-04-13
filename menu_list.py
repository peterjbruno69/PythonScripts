#menus = [ ['Egg Sandwhich', 'Bagel', 'Coffee'],
#          ['BLT', 'PB&J', 'Turkey Sandwich'],
#          ['Soup', 'Salad', 'Spaghetti', 'Taco'] ]

#print(menus[2][2])


menus = { 'Breakfast': ['Egg Sandwhich', 'Bagel', 'Coffee'],
          'Lunch':     ['BLT', 'PB&J', 'Turkey Sandwich'],
          'Dinner':    ['Soup', 'Salad', 'Spaghetti', 'Taco'] } 

for name, menu in menus.items():
    print(name, ':', menu)
