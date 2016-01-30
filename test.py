import os
import spc
import traceback

tfile = 0
tpass = 0

dpath = os.path.join(os.getcwd(), 'spc', 'test_data')
files = [f for f in os.listdir(dpath) if os.path.isfile(os.path.join(dpath, f))]
for f in files:
    tfile += 1
    try:
        f1 = spc.File(os.path.join(dpath, f))
        try:
            outfile = os.path.join(dpath, 'csv', f[:-4] + '.csv')
            with open(outfile, 'r') as fin:
                dat = fin.read()
                if f1.data_txt() == dat:
                    print("-->Pass")
                    tpass += 1
                else:
                    print("-->Fail")
        except:
            traceback.print_exc()
            print("--Fail")
    except:
        traceback.print_exc()
        print("-->Fail")
print("Passed %i of %i tests " % (tpass, tfile))
