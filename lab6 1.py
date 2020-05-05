import csv

def compound_properties(csv_name, compound_formula):
  """(str, str) -> tuple
  This function takes two parameters: the csv filename and the formula of the compound.

  It should call the molform() function to get the composition of the molecule and
  get the required property from the csv file. The csv file will have all the
  properties required.

  This function is required to return a tuple of three properties:
  1. The NAME of the atom with the lowest boiling point. 
      For example, if it's oxygen, return 'Oxygen', not 'O'
  2. The average (mean) of the atoms' boiling point in the molecule, round to the nearest integer
      For example, for FeSO4, it's the average boiling point of Fe, S and O,
      do not multiply the boiling point by the number of the atoms
  3. The molecular mass of the compound, round to the nearest integer
      For example, C1O2 (carbon dioxide) has weight of 12*1+16*2 = 44
  """
  compound_dict = molform(compound_formula)
  d = {}
  with open(csv_name, "r") as myfile:
    myfile.readline()
    for line in myfile:
      line_lst = line.split(',')
      symbol = line_lst[1].strip()
      name = line_lst[2].strip()
      atomic_mass = line_lst[3].strip()
      boiling_point = line_lst[4].strip()
      d[symbol] = (name, atomic_mass, boiling_point)
  bp = [ ]
  molecular_mass = 0.0
  for key in compound_dict:
    bp.append(float(d[key][2]))
    atom_mas = float(d[key][1])
    mol_mas = atom_mas * float(compound_dict[key])
    molecular_mass += float(atom_mas) * float(compound_dict[key])
  mean_bp = sum(bp) / len(bp)
  min_bp = min(bp)
  for k in compound_dict:
    if  float(d[k][2]) == float(min_bp):
      name = d[k][0]
  return (name,round(mean_bp),round(molecular_mass))
    
def molform(compound_formula):
  """(str) -> dictionary
  When passed a string of the compound formula, returns a dictionary
  with the elements as keys and the number of atoms of that element as values.
  When the string is empty, return an empty dictionary

  >>> molform("C2H6O1")
  {'C': 2, 'H': 6, 'O': 1}
  >>> molform("Cr1H4")
  {'Cr': 1, 'H': 4}
  >>> molform("C132983H211861N36149O40883S693")
  {'C': 132983, 'H': 211861, 'N': 36149, 'O': 40883, 'S': 693}
  """
  compound = { }
  elemnt = ''
  order = ''
  for i in range(len(compound_formula)-1):
    if compound_formula[i].isdigit( ) and compound_formula[i+1].isalpha( ):    
      order += compound_formula[i]
      compound[elemnt] = order
      elemnt = ''
      order = ''
    elif compound_formula[i].isalpha( ):
      elemnt += compound_formula[i]
    elif compound_formula[i].isdigit( ):
      order += compound_formula[i]
  compound[elemnt] = order + compound_formula[-1]  
  return compound