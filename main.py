from pycalphad import Database, calculate, equilibrium
import pycalphad.variables as v

db_path = "Unary.tdb"
db = Database(db_path)

if __name__ == "__main__":
    phases_names = db.phases.keys()
    comps = ['CU', 'VA']

    eq = equilibrium(dbf=db, comps=comps, phases=['BCC_A2', 'FCC_A1'], conditions={v.P: 101325, v.T: 500}, )
    print(eq)
    print('s')
