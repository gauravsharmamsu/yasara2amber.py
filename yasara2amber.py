###############################################################################
# yasara2amber.py
# 05/08/2021
# Gaurav Sharma
#
# Usage: 
# python yasara2amber.py
#
# Description:
# The script can convert the PDB files ontrained from yasara software to amber software. 
###############################################################################

with open('yasara.pdb', 'r') as file :
        filedata = file.read()
        filedata = filedata.replace('1H   THR', ' H1  THR') #edit the '1H   THR' to 'H1  THR'
        filedata = filedata.replace('2H   THR', ' H2  THR')
        filedata = filedata.replace('3H   THR', ' H3  THR')
        filedata = filedata.replace('1HB  ARG', '3HB  ARG')
        filedata = filedata.replace('1HG  ARG', '3HG  ARG')
        filedata = filedata.replace('1HD  ARG', '3HD  ARG')
        filedata = filedata.replace('1HB  ASP', '3HB  ASP')
        filedata = filedata.replace('1HB  GLN', '3HB  GLN')
        filedata = filedata.replace('1HG  GLN', '3HG  GLN')
        filedata = filedata.replace('1HB  ASN', '3HB  ASN')
        filedata = filedata.replace('1HA  GLY', '3HA  GLY')
        filedata = filedata.replace('1HB  TRP', '3HB  TRP')
        filedata = filedata.replace('1HB  GLU', '3HB  GLU')
        filedata = filedata.replace('1HG  GLU', '3HG  GLU')
        filedata = filedata.replace('1HB  MET', '3HB  MET')
        filedata = filedata.replace('1HG  MET', '3HG  MET')
        filedata = filedata.replace('1HB  SER', '3HB  SER')
        filedata = filedata.replace('1HB  ASN', '3HB  ASN')
        filedata = filedata.replace('1HB  GLU', '3HB  GLU')
        filedata = filedata.replace('1HG  GLU', '3HG  GLU')
        filedata = filedata.replace('1HB  PHE', '3HB  PHE')
        filedata = filedata.replace('1HA  GLY', '3HA  GLY')
        filedata = filedata.replace('1HB  TYR', '3HB  TYR')
        filedata = filedata.replace('1HB  LYS', '3HB  LYS')
        filedata = filedata.replace('1HG  LYS', '3HG  LYS')
        filedata = filedata.replace('1HD  LYS', '3HD  LYS')
        filedata = filedata.replace('1HE  LYS', '3HE  LYS')
        filedata = filedata.replace('1HB  LEU', '3HB  LEU')
        filedata = filedata.replace('1HB  ASP', '3HB  ASP')
        filedata = filedata.replace('1HB  HIS', '3HB  HIS')
        filedata = filedata.replace('1HB  CYS', '3HB  CYS')
        filedata = filedata.replace('1HG1 ILE', '2HG1 ILE')
        filedata = filedata.replace('2H   HOH', 'H2   WAT')
        filedata = filedata.replace('1H   HOH', 'H1   WAT')
        filedata = filedata.replace('O   HOH', 'O   WAT')
        with open('amber.pdb', 'w') as file:
                        file.write(filedata)
