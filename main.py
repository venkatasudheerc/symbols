# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import symbolVal


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    years = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
             '2014',
             '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    years = ['2023']
    i = 0
    for year in years[i:]:
        print(year)
        validator = symbolVal.SymbolVal(year)
        validator.evaluate()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
